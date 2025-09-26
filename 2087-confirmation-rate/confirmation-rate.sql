-- select user_id, 
-- ROUND(SUM(if(action="confirmed",1,0))/count(user_id),2) as confirmation_rate
-- from confirmations 
-- group by 1
-- union 
-- select user_id, 0.00 as confirmation_rate from signups where user_id not in (
--     select distinct user_id from confirmations
-- )

-- select s.user_id, ROUND(AVG(CASE
-- WHEN c.action="confirmed" THEN 1 ELSE 0
-- END),2) as confirmation_rate
-- from signups s
-- left join 
-- Confirmations c
-- on s.user_id=c.user_id
-- group by 1

-- if(c.action="confirmed",1,0)











-- with CTE as (
-- select *, 
-- COUNT(user_id) as tot_tr,
-- SUM(CASE WHEN action="confirmed" THEN 1 ELSE 0 END) as cf_tr
-- from confirmations 
-- group by user_id
-- )

-- select s.user_id, 
-- ROUND(IFNULL(c.cf_tr/c.tot_tr, 0), 2) as confirmation_rate 
-- from signups s 
-- left join CTE c 
-- on 
-- s.user_id = c.user_id










-- with CTE as (
--     select
--     user_id, 
--     SUM(CASE 
--     WHEN action = 'confirmed' THEN 1 else 0
--     END) as conf_count, 
--     count(*) as tot_trans
--     from confirmations
--     group by user_id
-- )
-- select s.user_id, 
-- ROUND(CASE 
--     WHEN (c.conf_count/c.tot_trans) is null THEN 0 
--     ELSE (c.conf_count/c.tot_trans)
-- END, 2) as confirmation_rate 
-- from 
-- Signups s 
-- left join 
-- CTE c 
-- on s.user_id = c.user_id






























with CTE as (
select user_id, 
SUM(
CASE WHEN action='confirmed' THEN 1 ELSE 0 END) as confirmed_tot, 
COUNT(1) as tot
from Confirmations
group by 1
)

select s.user_id, 
IFNULL(ROUND((c.confirmed_tot/tot),2),0) as confirmation_rate
from Signups s 
left join 
CTE c
on s.user_id = c.user_id
