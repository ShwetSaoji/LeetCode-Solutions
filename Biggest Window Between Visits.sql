# Write your MySQL query statement below
with CTE as (
select user_id, visit_date,
CASE
    WHEN ISNULL(LEAD(visit_date) OVER(PARTITION BY user_id ORDER BY visit_date)) THEN '2021-1-1'
    ELSE LEAD(visit_date) OVER(PARTITION BY user_id ORDER BY visit_date) 
END as next_date
from UserVisits
)

select user_id, MAX(DATEDIFF(next_date,visit_date)) as biggest_window
from CTE group by user_id
