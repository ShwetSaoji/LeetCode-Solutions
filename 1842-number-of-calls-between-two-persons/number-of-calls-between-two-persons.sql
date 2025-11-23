# Write your MySQL query statement below
select 
CASE
    WHEN from_id < to_id THEN from_id
    ELSE to_id 
END as person1, 
CASE
    WHEN from_id > to_id THEN from_id
    ELSE to_id 
END as person2, 
COUNT(*) as call_count, 
SUM(duration) as total_duration 
from Calls
group by 1, 2 