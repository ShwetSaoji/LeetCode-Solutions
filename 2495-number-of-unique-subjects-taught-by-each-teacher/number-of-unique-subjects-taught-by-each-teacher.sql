-- # Write your MySQL query statement below
-- -- select teacher_id, COUNT(distinct subject_id) as cnt from teacher 
-- -- group by 1


-- select DATE(NOW())









select teacher_id, count(distinct(subject_id)) as cnt 
from Teacher 
group by 1