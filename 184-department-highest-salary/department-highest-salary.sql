# Write your MySQL query statement below
with CTE as (
select e.name as employee ,e.salary,d.name as department, 
RANK () OVER(partition by e.departmentId ORDER BY e.salary desc) as rnk
from employee e
left join 
department d
on e.departmentid = d.id
)
select department,employee, salary from CTE where rnk=1