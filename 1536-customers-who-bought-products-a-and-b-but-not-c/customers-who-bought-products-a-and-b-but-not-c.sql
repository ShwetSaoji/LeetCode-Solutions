# Write your MySQL query statement below

with CTE as (
select distinct o1.customer_id from Orders o1
inner join orders o2 
on o1.customer_id = o2.customer_id and 
o1.product_name = 'A' and 
o2.product_name = 'B')

select c.customer_id, cus.customer_name from CTE c 
inner join 
Customers cus 
on c.customer_id = cus.customer_id 
where c.customer_id not in (select customer_id from Orders where product_name = 'C')