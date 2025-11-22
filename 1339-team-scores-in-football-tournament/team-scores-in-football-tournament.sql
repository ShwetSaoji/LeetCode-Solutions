# Write your MySQL query statement below
with CTE as (select team_id, SUM(points) as num_points from (
select host_team as team_id, 
CASE
WHEN host_goals > guest_goals THEN 3
WHEN host_goals < guest_goals THEN 0 
ELSE 1
END as points 
from Matches
union all
select guest_team as team_id, 
CASE
WHEN guest_goals > host_goals THEN 3
WHEN guest_goals < host_goals THEN 0 
ELSE 1
END as points 
from Matches) a
group by team_id)

select t.*, 
IFNULL(c.num_points,0) as num_points from 
Teams t 
left join 
CTE c 
on t.team_id = c.team_id 
order by 3 desc , 1