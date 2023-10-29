# Write your MySQL query statement below

with aa as 
(
select reports_to, COUNT(reports_to) as reports_count,
ROUND(AVG(age)) average_age from Employees 
group by reports_to having reports_count > 0
)
select e.employee_id, e.name, aa.reports_count, aa.average_age
from Employees e
inner join 
aa 
on e.employee_id = aa.reports_to
order by employee_id
