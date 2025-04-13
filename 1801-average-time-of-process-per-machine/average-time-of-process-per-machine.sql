-- select a1.machine_id, ROUND(AVG(a2.timestamp-a1.timestamp),3) as processing_time
-- from activity a1
-- join 
-- activity a2
-- on a1.machine_id = a2.machine_id
-- and
-- a1.activity_type="start" 
-- and
-- a2.activity_type="end"
-- group by a1.machine_id






with CTE as (
select a1.machine_id, a1.process_id, ROUND((a2.timestamp - a1.timestamp),3) as pro_time
from Activity a1
join 
Activity a2 on
a1.machine_id = a2.machine_id and
a1.process_id = a2.process_id and
a1.activity_type = "start" and
a2.activity_type = "end"
group by 1, 2
)

select machine_id, 
ROUND(SUM(pro_time)/(select count(distinct process_id) from Activity), 3) as processing_time
from CTE 
group by 1



