# Write your MySQL query statement below

with sales as (
select *, 
SUM(amount) OVER(PARTITION BY visited_on) as day_sales,
RANK() OVER(PARTITION BY visited_on ORDER BY customer_id) as rnk
from Customer),
week_sales as (
select visited_on,
SUM(day_sales) OVER(ORDER BY visited_on rows between 6 preceding and current row) as amount,
ROUND(AVG(day_sales) OVER(ORDER BY visited_on rows between 6 preceding and current row),2) as average_amount
from sales
where rnk = 1 )


select * from week_sales where DATEDIFF(visited_on, (select MIN(visited_on) from Customer)) >= 6

-- select MIN(visited_on) from Customer