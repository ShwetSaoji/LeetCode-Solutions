# Write your MySQL query statement below
# select ROUND(SUM(if(MIN(order_date)=MIN(customer_pref_delivery_date),1,0))*100/(select count(distinct(customer_id)) from Delivery),2)
# from Delivery 
# group by customer_id



select ROUND(SUM(if(b.min_od=b.min_dd, 1, 0))*100/(select count(distinct(customer_id)) from Delivery),2) as immediate_percentage from 
(
select MIN(order_date) as min_od, MIN(customer_pref_delivery_date) as min_dd
from Delivery
group by customer_id
) as b
