# Write your MySQL query statement below

with CTE as (
select *, 
RANK() OVER(PARTITION BY player_id ORDER BY event_date) as rnk,
LEAD(event_date) OVER(PARTITION BY player_id ORDER BY event_date) as next_login
from Activity)

select ROUND((select COUNT(*) from CTE where rnk = 1 and DATEDIFF(next_login, event_date) = 1)/
(select COUNT(DISTINCT player_id) from Activity),2) as fraction 