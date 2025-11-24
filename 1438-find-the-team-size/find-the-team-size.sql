# Write your MySQL query statement below
with team_strenght as (
    select team_id, count(*) as team_size from Employee group by 1
)

select e.employee_id, ts.team_size from Employee e 
join team_strenght ts
on e.team_id = ts.team_id