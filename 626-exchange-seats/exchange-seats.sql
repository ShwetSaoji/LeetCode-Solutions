# Write your MySQL query statement below

with CTE as (
select *, 
LAG(student) OVER(ORDER BY id) as prev_student, 
LEAD(student) OVER(ORDER BY id) as nxt_student
from Seat)

select id, 
CASE
    WHEN id%2 = 1 and nxt_student is null THEN student
    WHEN id%2 = 1 THEN nxt_student
    ELSE prev_student
END as student
from CTE