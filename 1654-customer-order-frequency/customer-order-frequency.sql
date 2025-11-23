# Write your MySQL query statement below
select c.customer_id, c.name from Customers c 
join Orders o 
on c.customer_id = o.customer_id 
join Product p
on o.product_id = p.product_id
group by 1 
having 
SUM(if(o.order_date like '2020-06%', o.quantity * p.price, 0)) >= 100
AND 
SUM(if(o.order_date like '2020-07%', o.quantity * p.price, 0)) >= 100