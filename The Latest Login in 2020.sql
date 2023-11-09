# Write your MySQL query statement below

select user_id, MAX(time_stamp) as last_stamp from Logins 
where time_stamp like '2020-%'
group by 1
