# Write your MySQL query statement below


select product_id, year as first_year, quantity, price from (
select *, 
RANK() OVER(PARTITION BY product_id ORDER BY year) as rnk 
from Sales) A
where rnk = 1