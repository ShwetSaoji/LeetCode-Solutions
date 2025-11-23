# Write your MySQL query statement below
select w.name as warehouse_name , SUM(w.units*p.Width*p.Length*p.Height) as volume 
from 
Warehouse w 
inner join 
Products p 
on 
w.product_id = p.product_id 
group by 1