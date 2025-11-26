# Write your MySQL query statement below
with CTE as (
select customer_id, product_id, 
COUNT(1) as cnt 
from Orders 
group by 1, 2 ), 
CTE2 as (
    select customer_id, product_id, 
    RANK() OVER(PARTITION BY customer_id ORDER BY cnt desc) as rnk
    from CTE
)

select c.customer_id, c.product_id, p.product_name from CTE2 c
inner join 
Products p 
on c.product_id = p.product_id where c.rnk = 1
