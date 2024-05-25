with CTE as (
select *, 
LAG(event_date) OVER(partition by player_id order by event_date) as prev_login,
RANK() OVER(partition by player_id order by event_date) as rnk
from activity 
)

select ROUND((select count(*) from CTE where rnk = 2 and DATEDIFF(event_date, prev_login) = 1)/
(select count(distinct player_id) from activity),2) as fraction