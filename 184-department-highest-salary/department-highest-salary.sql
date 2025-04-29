# Write your MySQL query statement below

with CTE as (
select *, 
RANK() OVER(PARTITION BY departmentId order by salary desc) as rnk 
from Employee)

select d.name as Department, c.name as Employee, c.salary as Salary 
from CTE c 
inner join 
Department d 
on c.departmentId = d.id
where c.rnk=1