# Write your MySQL query statement below
with CTE as (
select e1.*, e2.salary as manager_sal from Employee e1 
inner join Employee e2 
on e1.managerId = e2.id
)

select name as Employee from CTE where salary > manager_sal
