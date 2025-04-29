# Write your MySQL query statement below

with CTE as (
select *, 
LEAD(event_date) OVER(PARTITION BY player_id ORDER BY event_date) as next_login,
RANK() OVER(PARTITION BY player_id order by event_date) as rnk
from Activity)

select 
ROUND((select count(distinct player_id) from CTE where DATEDIFF(next_login, event_date) = 1 and rnk=1)/
(select count(distinct player_id) from Activity),2)
as fraction


-- select DATEDIFF('2025-05-02', '2023-05-01')