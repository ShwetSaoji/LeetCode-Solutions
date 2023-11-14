# Write your MySQL query statement below
with CTE as (
select team_id, count(*) as team_size from Employee 
group by team_id
)

select e.employee_id, c.team_size from employee e 
inner join CTE c 
on 
e.team_id=c.team_id
