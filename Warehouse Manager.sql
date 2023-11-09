# Write your MySQL query statement below

select w.name as warehouse_name, 
SUM(w.units*p.width*p.length*p.height) as volume
from warehouse w
join 
products p 
on w.product_id = p.product_id
group by w.name
