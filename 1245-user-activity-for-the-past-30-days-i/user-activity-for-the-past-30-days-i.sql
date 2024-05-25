select activity_date as day, COUNT(distinct user_id) as active_users from activity
where activity_date > "2019-06-27" and activity_date <= "2019-07-27"
group by 1