# Write your MySQL query statement below

with CTE as (
select *, 
SUM(weight) OVER(ORDER BY turn) as roll_weight
from Queue)

select person_name from CTE where roll_weight <= 1000
order by turn desc LIMIT 1