# Write your MySQL query statement below
select a1.sale_date, (a2.sold_num-a1.sold_num) as diff 
from sales a1
join 
sales a2
on 
a1.sale_date=a2.sale_date and a1.fruit!=a2.fruit
group by sale_date
order by sale_date
