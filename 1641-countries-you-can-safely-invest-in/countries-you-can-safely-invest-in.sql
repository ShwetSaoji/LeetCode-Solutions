# Write your MySQL query statement below

with CTE as (
select p.*, c.name as country from 
Person p 
inner join 
country c 
on SUBSTRING(p.phone_number, 1, 3) = c.country_code),
CTE2 as (
select c.country, AVG(ca.duration) as cntry_avg
from CTE c 
inner join 
calls  ca
on c.id = ca.caller_id or c.id = ca.callee_id
group by 1)

select country from CTE2 where cntry_avg > (select AVG(duration) from calls)

-- select AVG(duration) from calls