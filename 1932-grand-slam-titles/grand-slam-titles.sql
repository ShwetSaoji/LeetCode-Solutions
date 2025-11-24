# Write your MySQL query statement below
with CTE as (
select winner as player_id, COUNT(winner) as grand_slams_count from (
select Wimbledon as winner from Championships
union all
select Fr_open as winner from Championships
union all
select US_open as winner from Championships
union all
select Au_open as winner from Championships) a 
group by 1 )

select c.player_id, p.player_name, c.grand_slams_count
from CTE c
join Players p
on c.player_id = p.player_id