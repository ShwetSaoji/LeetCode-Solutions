# Write your MySQL query statement below

with CTE as (
select *, 
RANK() OVER(PARTITION BY user_id ORDER BY activity_date) as first_login
from Traffic
where activity = 'login'
)

select activity_date as login_date, COUNT(distinct user_id) as user_count
from CTE 
where first_login = 1  
and DATEDIFF('2019-06-30', activity_date) <= 90
group by activity_date