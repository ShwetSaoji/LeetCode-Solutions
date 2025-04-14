-- with CTE as (
--     select num, 
--     LAG(num) OVER(order by id) as prev,
--     LEAD(num) OVER(order by id) as next
--     from Logs
-- )

-- select distinct(num) as ConsecutiveNums from CTE where num = prev and num = next















with CTE as (
select *, 
LAG(num) OVER(ORDER BY id) as prev,
LEAD(num) OVER(ORDER BY id) as next
from Logs)
select distinct num as ConsecutiveNums from CTE where
num = prev and num = next