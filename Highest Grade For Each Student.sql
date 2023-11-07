# Write your MySQL query statement below
with CTE as (
select student_id, max(grade) as grade from Enrollments
group by 1 order by 1
)

select c.student_id,min(e.course_id) as course_id, c.grade from 
CTE c 
inner join 
Enrollments e
on c.student_id=e.student_id and c.grade=e.grade
group by c.student_id
order by student_id
