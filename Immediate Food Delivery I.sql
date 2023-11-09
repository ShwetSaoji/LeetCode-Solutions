select ROUND(SUM(if(order_date=customer_pref_delivery_date,1,0))*100/count(*),2) as immediate_percentage from Delivery
