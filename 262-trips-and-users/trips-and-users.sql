# Write your MySQL query statement below

with unbanned as (
select * from Trips where client_id not in (
    select users_id from Users where banned = 'Yes'
) and driver_id not in (
    select users_id from Users where banned = 'Yes'
) ),
CTE2 as (
select request_at as Day, 
SUM(CASE
    WHEN status='cancelled_by_driver' or status='cancelled_by_client' THEN 1 ELSE 0
END ) as cancelled_rides,
COUNT(1) as total_rides
from unbanned 
group by request_at)

select Day, ROUND(cancelled_rides/total_rides,2) as 'Cancellation Rate'
from CTE2 where Day between "2013-10-01" and "2013-10-03"
