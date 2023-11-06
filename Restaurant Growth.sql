# Write your MySQL query statement below
select visited_on , 
(
  select sum(amount) from Customer where 
  visited_on between DATE_SUB(c.visited_on, INTERVAL 6 DAY) and c.visited_on
) AS AMOUNT,
(
  select ROUND(SUM(amount)/7,2) from customer where 
  visited_on between DATE_SUB(c.visited_on, INTERVAL 6 DAY) and c.visited_on
) as average_amount
from customer c
where c.visited_on >=
( select DATE_ADD(MIN(visited_on), INTERVAL 6 DAY) from customer)
group by visited_on
