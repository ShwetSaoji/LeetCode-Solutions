# Write your MySQL query statement below

with CTE as (
select user_id, 
ROUND(SUM(CASE
    WHEN action = 'confirmed' THEN 1 ELSE 0 
END)/COUNT(1),2) as confirmation_rate
from Confirmations
group by user_id)

select s.user_id, IFNULL(c.confirmation_rate,0) as confirmation_rate
from Signups s 
left join 
CTE c
on s.user_id = c.user_id