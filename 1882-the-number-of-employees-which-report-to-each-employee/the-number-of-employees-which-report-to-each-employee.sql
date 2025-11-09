# Write your MySQL query statement below
-- select e1.employee_id, e1.name, 
-- COUNT(e2.reports_to) as reports_count,
-- ROUND(AVG(e2.age)) as average_age
-- from employees e1
-- join 
-- employees e2
-- on 
-- e1.employee_id = e2.reports_to
-- group by e2.reports_to
-- order by 1








-- with CTE as (
--     select reports_to, count(reports_to) as reports_count, ROUND(AVG(age)) as average_age
--     from Employees
--     where reports_to is not null
--     group by reports_to
-- )
-- select c.reports_to as employee_id, e.name, c.reports_count, c.average_age
-- from CTE c
-- join Employees e
-- on c.reports_to = e.employee_id
-- order by 1



















-- with CTE as (
-- select reports_to, COUNT(reports_to) as reports_count, ROUND(AVG(age)) as average_age
-- from Employees e 
-- where reports_to is not null
-- group by 1
-- )

-- select c.reports_to as employee_id, e.name, c.reports_count, c.average_age 
-- from CTE c 
-- inner join 
-- EMployees e 
-- on c.reports_to = e.employee_id
-- order by 1





select mgr.employee_id, mgr.name, COUNT(emp.employee_id) as reports_count, ROUND(AVG(emp.age)) as average_age
from employees emp 
join employees mgr
on emp.reports_to = mgr.employee_id
group by 1
order by 1