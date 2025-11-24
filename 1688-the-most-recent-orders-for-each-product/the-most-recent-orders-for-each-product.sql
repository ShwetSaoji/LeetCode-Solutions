# Write your MySQL query statement below

with CTE as (select product_id, order_id, order_date, 
RANK() OVER(PARTITION BY product_id ORDER BY order_date desc) as rnk
from Orders )

select p.product_name, c.product_id, c.order_id, c.order_date
from CTE c
inner join 
Products p 
on c.product_id = p.product_id 
where c.rnk = 1
order by 1, 2, 3