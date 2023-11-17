# Write your MySQL query statement below
with CTE as (
    select order_id, customer_id, order_date,
    RANK() OVER(
        PARTITION BY customer_id
        ORDER BY order_date DESC
    ) as rnk
    from orders
)

select cc.name as customer_name , c.customer_id, c.order_id , c.order_date from CTE c
join 
Customers cc
on 
c.customer_id=cc.customer_id and c.rnk <= 3
order by 1 , 2, 4 DESC
