# Write your MySQL query statement below
# select stu.student_id, stu.student_name, e.subject_name, count(e.subject_name) as attended_exams from 
# Students stu
# inner join 
# Examinations e 
# on stu.student_id = e.student_id
# group by 1,2,3
# order by student_id, subject_name


select s.student_id, s.student_name, sub.subject_name, IFNULL(grouped.attended_exams, 0) as attended_exams
from students s
cross join subjects sub
left join 
(select student_id, subject_name, count(*) as attended_exams from Examinations
group by 1, 2) as grouped
on s.student_id = grouped.student_id and sub.subject_name = grouped.subject_name
order by student_id, subject_name 
