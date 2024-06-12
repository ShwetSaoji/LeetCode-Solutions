-- select user_id, 
-- ROUND(SUM(if(action="confirmed",1,0))/count(user_id),2) as confirmation_rate
-- from confirmations 
-- group by 1
-- union 
-- select user_id, 0.00 as confirmation_rate from signups where user_id not in (
--     select distinct user_id from confirmations
-- )

select s.user_id, ROUND(AVG(CASE
WHEN c.action="confirmed" THEN 1 ELSE 0
END),2) as confirmation_rate
from signups s
left join 
Confirmations c
on s.user_id=c.user_id
group by 1

-- if(c.action="confirmed",1,0)