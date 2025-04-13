-- select stu.student_id, stu.student_name,
-- sub.subject_name,
-- count(e.subject_name) as attended_exams from Students stu
-- cross join 
-- subjects sub
-- left join 
-- examinations e
-- on stu.student_id = e.student_id
-- and sub.subject_name = e.subject_name
-- group by 1,3
-- order by 1,3










select stu.student_id, stu.student_name, sub.subject_name,
count(e.student_id) as attended_exams
from students stu
cross join 
subjects sub
left join 
examinations e
on stu.student_id = e.student_id and
sub.subject_name = e.subject_name
group by 1, 3
order by 1, 3

-- select s.student_id, s.student_name, sub.subject_name,
-- COUNT(e.subject_name) as attended_exams
-- from students s cross join subjects sub
-- left join examinations e
-- on s.student_id = e.student_id and sub.subject_name = e.subject_name
-- group by 1, 3
-- order by 1, 3