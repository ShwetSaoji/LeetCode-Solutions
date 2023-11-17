# Write your MySQL query statement below
with CTE as (
    select name, salary , departmentId, 
    RANK() OVER (
        PARTITION BY departmentId
        ORDER BY salary DESC
    ) as rnk
    from Employee
)

select d.name as department, c.name as employee, c.salary from CTE c
join department d
on c.departmentId = d.id
and c.rnk = 1
