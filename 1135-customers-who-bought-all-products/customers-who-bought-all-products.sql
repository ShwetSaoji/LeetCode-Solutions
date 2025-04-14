-- # Write your MySQL query statement below
-- -- with CTE as (
-- --     select customer_id, count(distinct product_key) as products 
-- --     from customer
-- --     group by 1
-- -- )

-- -- select customer_id from CTE where products = (select count(*) from Product)

-- select customer_id from customer group by 1 having count(distinct product_key) = (select count(*) from Product)




select customer_id from customer group by 1 having count(distinct(product_key)) = (select count(*) from Product)



