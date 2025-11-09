# Write your MySQL query statement below

-- select a1.machine_id, ROUND(AVG(a2.timestamp-a1.timestamp), 3) as abc
-- from activity a1
-- inner join 
-- activity a2
-- on a1.machine_id = a2.machine_id
-- and m1.process

select a1.machine_id, ROUND(AVG(a2.timestamp-a1.timestamp),3) as processing_time
from activity a1
join 
activity a2
on a1.machine_id = a2.machine_id
and
a1.activity_type="start" 
and
a2.activity_type="end"
group by a1.machine_id