# Write your MySQL query statement below

select machine_id, 
ROUND(SUM(CASE WHEN activity_type='start' THEN timestamp*-1 ELSE timestamp END)
/(select count(distinct process_id)),3) as processing_time
from Activity
group by 1
