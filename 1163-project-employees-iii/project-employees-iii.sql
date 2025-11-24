# Write your MySQL query statement below

select project_id, employee_id from (
select p.*, 
RANK() OVER(PARTITION BY p.project_id ORDER BY e.experience_years desc) as rnk 
from Project p 
inner join Employee e 
on p.employee_id = e.employee_id) a 
where rnk = 1
