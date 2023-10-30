# Write your MySQL query statement below

select employee_id from Employees where
salary < 30000 and manager_id not in 
(select distinct employee_id from Employees)
order by employee_id
