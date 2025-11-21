# Write your MySQL query statement below
select c.* from Customers c
join 
Orders o 
on c.customer_id = o.customer_id
where o.product_name in ('A', 'B') and 
c.customer_id not in (
    select customer_id from Orders where product_name = 'C'
)
group by c.customer_name having count(distinct o.product_name) > 1
order by c.customer_id