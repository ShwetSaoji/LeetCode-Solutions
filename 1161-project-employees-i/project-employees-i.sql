-- select p.project_id, ROUND(AVG(e.experience_years),2) as average_years
-- from 
-- Project p
-- left join 
-- employee e
-- on p.employee_id = p.employee_id
-- group by 1

select p.project_id, ROUND(AVG(e.experience_years),2) as average_years 
from Project p 
join 
Employee e 
on 
p.employee_id = e.employee_id
group by 1