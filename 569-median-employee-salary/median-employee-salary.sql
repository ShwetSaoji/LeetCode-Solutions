# Write your MySQL query statement below


with CTE as (
select *, 
ROW_NUMBER() OVER(PARTITION BY company ORDER BY salary) as rn 
from Employee),
CTE2 as (
select *, 
(MAX(rn) OVER(PARTITION BY company))/2 as lower_end,
(MAX(rn) OVER(PARTITION BY company))/2+1 as upper_end 
from CTE)

select id, company, salary from CTE2 where rn between lower_end and upper_end
-- select * from CTE2
