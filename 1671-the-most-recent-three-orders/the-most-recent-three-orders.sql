# Write your MySQL query statement below

with t as (
    select 
        order_id, 
        order_date, 
        customer_id, 
        row_number() over (
            partition by customer_id
            order by order_date desc
        ) as rn 
    from orders 
)

select 
    name as customer_name, 
    t.customer_id,  
    order_id, 
    order_date
from t 
join customers as c
on t.customer_id = c.customer_id
where rn <= 3
order by name, t.customer_id, order_date desc 