# Write your MySQL query statement below


with CTE as (
select num, 
LAG(num) OVER(ORDER BY id) as prev,
LEAD(num) OVER(ORDER BY id) as nxt 
from Logs)

select distinct num as ConsecutiveNums from CTE where 
num = prev and num = nxt