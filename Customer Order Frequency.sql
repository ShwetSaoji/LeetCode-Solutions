select customer_id, name from 
(
select o.customer_id, c.name, 
SUM(
    CASE
        WHEN o.order_date like '2020-06%' THEN p.price*o.quantity 
        ELSE 0
    END
) as t1,
SUM(
    CASE
        WHEN o.order_date like '2020-07%' THEN p.price*o.quantity 
        ELSE 0
    END
) as t2
from customers c
JOIN 
orders o
on 
c.customer_id=o.customer_id
JOIN
product p
on o.product_id=p.product_id
group by 1
having t1 >= 100 and t2>=100
)tmp
