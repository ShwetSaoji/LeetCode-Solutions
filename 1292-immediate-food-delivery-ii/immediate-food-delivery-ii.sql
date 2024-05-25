with CTE as (select *, 
RANK() OVER(partition by customer_id order by order_date) as rnk
from 
delivery)

select ROUND((select count(*) from CTE where order_date = customer_pref_delivery_date and rnk=1)*100/
(select count(distinct customer_id) from delivery),2) as immediate_percentage

