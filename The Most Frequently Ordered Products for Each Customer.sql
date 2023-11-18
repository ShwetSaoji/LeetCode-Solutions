# Write your MySQL query statement below
with CTE AS (
select *,
RANK() OVER(
    PARTITION BY customer_id 
    ORDER BY count(product_id) DESC
) as rnk
from orders
group by customer_id, product_id
)

select c.customer_id, c.product_id, p.product_name 
from CTE c 
join products p
on c.product_id=p.product_id
and c.rnk = 1
