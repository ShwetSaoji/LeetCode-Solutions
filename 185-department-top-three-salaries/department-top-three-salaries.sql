# Write your MySQL query statement below


with CTE as (
select *, 
DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) as rnk 
from Employee)

select d.name as Department, c.name as Employee, c.salary as Salary
from CTE c 
inner join Department d
on c.departmentId = d.id
where rnk <=3