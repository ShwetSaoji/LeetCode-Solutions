-- -- with CTE as (
-- -- select *, 
-- -- LAG(event_date) OVER(partition by player_id order by event_date) as prev_login,
-- -- RANK() OVER(partition by player_id order by event_date) as rnk
-- -- from activity 
-- -- )

-- -- select ROUND((select count(*) from CTE where rnk = 2 and DATEDIFF(event_date, prev_login) = 1)/
-- -- (select count(distinct player_id) from activity),2) as fraction










-- -- select ROUND((select count(*) from activity a1 join activity a2
-- -- on a1.player_id = a2.player_id and a1.event_date = DATE_SUB(a2.event_date, INTERVAL 1 DAY))/
-- -- (select count(distinct player_id) from activity),2) as fraction 
-- select count(*) from activity a1 join activity a2
-- on a1.player_id = a2.player_id and a1.event_date = DATE_SUB(a2.event_date, INTERVAL 1 DAY)










with CTE as (
select player_id, event_date,
RANK() OVER(PARTITION BY player_id ORDER BY event_date) as rnk, 
LAG(event_date) OVER(PARTITION BY player_id ORDER BY event_date) as prev_login
from Activity
)

select ROUND((select count(*) from CTE where rnk = 2 and
DATEDIFF(event_date, prev_login) = 1)/(select count(distinct(player_id)) from Activity),2)
as fraction