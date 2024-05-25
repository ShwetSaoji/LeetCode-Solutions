select stu.student_id, stu.student_name,
sub.subject_name,
count(e.subject_name) as attended_exams from Students stu
cross join 
subjects sub
left join 
examinations e
on stu.student_id = e.student_id
and sub.subject_name = e.subject_name
group by 1,3
order by 1,3