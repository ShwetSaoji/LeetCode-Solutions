# Write your MySQL query statement below
with CTE as (
    select p.project_id,p.employee_id, 
    RANK() OVER(
        PARTITION BY p.project_id
        ORDER BY e.experience_years DESC
    ) as rnk
    from project p
    join 
    employee e
    on p.employee_id = e.employee_id
)

select project_id, employee_id from CTE where rnk = 1
