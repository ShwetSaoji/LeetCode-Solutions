

with CTE as (
select *, 
SUM(amount) as tot_amount
from customer 
group by visited_on),

CTE2 as (
select *,
SUM(tot_amount) OVER(order by visited_on rows between 6 PRECEDING and CURRENT ROW ) as tot_sum
from CTE
)


select visited_on, tot_sum as amount, ROUND((tot_sum/7),2) as average_amount
from CTE2
where visited_on >= (select DATE_ADD(MIN(visited_on), INTERVAL 6 DAY) from customer)
