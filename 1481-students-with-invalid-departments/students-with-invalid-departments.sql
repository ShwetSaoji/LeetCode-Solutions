# Write your MySQL query statement below
select s.id, s.name from Students s 
left join 
Departments d
on s.department_id = d.id 
where d.name is NULL