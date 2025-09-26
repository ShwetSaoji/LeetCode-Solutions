-- -- select stu.student_id, stu.student_name,
-- -- sub.subject_name,
-- -- count(e.subject_name) as attended_exams from Students stu
-- -- cross join 
-- -- subjects sub
-- -- left join 
-- -- examinations e
-- -- on stu.student_id = e.student_id
-- -- and sub.subject_name = e.subject_name
-- -- group by 1,3
-- -- order by 1,3










-- select stu.student_id, stu.student_name, sub.subject_name,
-- count(e.student_id) as attended_exams
-- from students stu
-- cross join 
-- subjects sub
-- left join 
-- examinations e
-- on stu.student_id = e.student_id and
-- sub.subject_name = e.subject_name
-- group by 1, 3
-- order by 1, 3

-- -- select s.student_id, s.student_name, sub.subject_name,
-- -- COUNT(e.subject_name) as attended_exams
-- -- from students s cross join subjects sub
-- -- left join examinations e
-- -- on s.student_id = e.student_id and sub.subject_name = e.subject_name
-- -- group by 1, 3
-- -- order by 1, 3








with CTE as (
select stu.student_id, stu.student_name, sub.subject_name 
from Students stu 
cross join 
Subjects sub)

select c.student_id, c.student_name, c.subject_name,  COUNT(e.student_id) as attended_exams
from CTE c
left join 
Examinations e
on c.student_id = e.student_id
and c.subject_name = e.subject_name
group by 1, 3 
order by 1, 3 


