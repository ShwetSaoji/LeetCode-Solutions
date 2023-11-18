# Write your MySQL query statement below
with CTE_LOGS as (
    select log_id, log_id - RANK() OVER(ORDER BY log_id) as dif
    from logs
)

select MIN(log_id) as start_id, MAX(log_id) as end_id from CTE_LOGS
group by dif

# select * from CTE_LOGS
