# Write your MySQL query statement below
select user_id, time_stamp as last_stamp from (
select * , 
RANK() OVER(PARTITION BY user_id ORDER BY time_stamp desc) as rnk 
from Logins 
where YEAR(time_stamp) = '2020') a 
where rnk = 1
