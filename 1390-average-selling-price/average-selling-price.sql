select p.product_id, IFNULL(ROUND(SUM(p.price*u.units)/SUM(u.units),2),0) as average_price
from prices p
left join 
unitssold u
on p.product_id = u.product_id
and u.purchase_date between p.start_date and p.end_date
group by 1