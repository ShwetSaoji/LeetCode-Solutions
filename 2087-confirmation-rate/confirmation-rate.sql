select user_id, 
ROUND(SUM(if(action="confirmed",1,0))/count(user_id),2) as confirmation_rate
from confirmations 
group by 1
union 
select user_id, 0.00 as confirmation_rate from signups where user_id not in (
    select distinct user_id from confirmations
)