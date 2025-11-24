# Write your MySQL query statement below
with CTE as (select log_id, 
row_number() over() as rn 
from Logs
), 
CTE2 as (
    select log_id, 
    abs(log_id - rn) as diff 
    from CTE
)
select MIN(log_id) as start_id, MAX(log_id) as end_id from CTE2
group by diff