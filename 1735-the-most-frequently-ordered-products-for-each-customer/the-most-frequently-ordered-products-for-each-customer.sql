# Write your MySQL query statement below


-- with CTE as (
-- select *, 
-- RANK() OVER(PARTITION BY customer_id order by order_date desc) as rnk 
-- from Orders 
-- order by customer_id)


-- select c.product_id, p.product_name, c.customer_id 
-- from CTE c 
-- inner join Products p 
-- on 
-- c.product_id = p.product_id
-- where c.rnk = 1


with CTE as (
select customer_id, product_id, count(1) as cnt 
from Orders 
group by 1, 2 ),
CTE2 as (
select customer_id, product_id from CTE where (customer_id, cnt) in (
    select customer_id, MAX(cnt) as cnt from CTE GROUP BY 1
))

select c.customer_id, c.product_id, p.product_name from 
CTE2 c 
inner join 
Products p 
on c.product_id = p.product_id