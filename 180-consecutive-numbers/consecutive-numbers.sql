# Write your MySQL query statement below

with CTE as (
select *, 
lAG(num) OVER(ORDER BY id) as prev_num,
LEAD(num) OVER(ORDER BY id) as next_num 
from Logs)

select distinct num as ConsecutiveNums from CTE 
where num = prev_num and num = next_num