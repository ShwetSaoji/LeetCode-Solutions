# Write your MySQL query statement below

select transaction_id from (
select transaction_id, 
RANK() OVER(PARTITION BY day ORDER BY amount desc) as rnk
from Transactions) a
where rnk = 1
order by 1