-- -- select activity_date as day, COUNT(distinct user_id) as active_users from activity
-- -- where activity_date > "2019-06-27" and activity_date <= "2019-07-27"
-- -- group by 1




-- select activity_date as day, COUNT(distinct user_id) as active_users from activity 
-- where activity_date <= "2019-07-27" and DATEDIFF("2019-07-27", activity_date) <= 30
-- group by 1












select activity_date as day, 
count(distinct(user_id)) as active_users 
from Activity
where activity_date between "2019-06-28" and "2019-07-27"
group by 1 