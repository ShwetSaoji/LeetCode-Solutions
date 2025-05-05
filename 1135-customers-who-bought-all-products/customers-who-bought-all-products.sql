# Write your MySQL query statement below

select customer_id from Customer group by 1
having COUNT(DISTINCT product_key) = (select count(1) from product) 
