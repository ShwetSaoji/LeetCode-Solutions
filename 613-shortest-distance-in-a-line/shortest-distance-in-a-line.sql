# Write your MySQL query statement below
with CTE as (
    select * from Point order by x
),
CTE2 as (
select *, 
LEAD(x) OVER(ORDER BY x) as nxt
from CTE )

select MIN(shortest) as shortest from (
    select abs(x - nxt) as shortest from CTE2
) a
