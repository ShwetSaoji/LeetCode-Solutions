# Write your MySQL query statement below

with top_scored_course as (select *, 
RANK() OVER(PARTITION BY student_id ORDER BY grade desc, course_id) as rnk
from Enrollments)

select student_id, course_id, grade  from top_scored_course where rnk = 1 order by 1 
-- select student_id, course_id, grade from top_scored_course where rnk = 1 
-- order by course_id 