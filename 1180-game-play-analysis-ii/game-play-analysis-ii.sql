# Write your MySQL query statement below

with CTE as (select player_id, device_id, 
RANK() OVER(PARTITION BY player_id ORDER BY event_date) as rnk 
from Activity)

select player_id, device_id from CTE where rnk = 1