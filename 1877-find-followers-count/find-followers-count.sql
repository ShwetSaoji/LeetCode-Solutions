-- # Write your MySQL query statement below
-- select user_id, count(user_id) as followers_count 
-- from followers 
-- group by 1 
-- order by 1










select user_id, count(follower_id) as followers_count 
from Followers 
group by 1 
order by 1