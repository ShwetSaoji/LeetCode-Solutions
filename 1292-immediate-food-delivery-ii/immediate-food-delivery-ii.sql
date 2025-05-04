# Write your MySQL query statement below
with CTE as (
select *, 
RANK() OVER(PARTITION BY customer_id ORDER BY order_date) as rnk,
CASE 
    WHEN order_date = customer_pref_delivery_date THEN 'immediate' ELSE 'scheduled'
END as order_type
from Delivery)

select ROUND((select count(1) from CTE where rnk = 1 and order_type = 'immediate')*100/
(select count(1) from CTE where rnk = 1),2) as immediate_percentage