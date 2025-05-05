# Write your MySQL query statement below


select distinct num as ConsecutiveNums  from ( 
select *, 
LAG(num) OVER(ORDER BY id) as prev, 
LEAD(num) OVER(ORDER BY id) as nxt 
from 
Logs) A 
where num = prev and num = nxt