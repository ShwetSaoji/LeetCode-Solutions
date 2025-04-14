-- -- with CTE as (select *, 
-- -- RANK() OVER(partition by customer_id order by order_date) as rnk
-- -- from 
-- -- delivery)

-- -- select ROUND((select count(*) from CTE where order_date = customer_pref_delivery_date and rnk=1)*100/
-- -- (select count(distinct customer_id) from delivery),2) as immediate_percentage




















-- with CTE as (
-- select *, 
-- RANK() OVER(PARTITION BY customer_id ORDER BY order_date) as rnk,
-- CASE WHEN customer_pref_delivery_date = order_date THEN "immediate" ELSE "SC" END as o_type
-- from delivery
-- )
-- select (select count(*) from CTE where rnk=1 and o_type="immediate")*100/(select count(*) from CTE where rnk = 1) as immediate_percentage








with CTE AS(
select order_date, customer_pref_delivery_date, 
RANK() OVER(PARTITION BY customer_id ORDER BY order_date) as rnk 
from Delivery)

select ROUND((select count(*) from CTE where rnk = 1 and order_date = customer_pref_delivery_date)*100/
(select count(distinct(customer_id)) from Delivery),2) as immediate_percentage