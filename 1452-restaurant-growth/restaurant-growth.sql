
-- -- with CTE as (
-- --     select *, 
-- --     SUM(amount) as tot_day_amount
-- --     from customer 
-- --     group by visited_on
-- -- )
-- -- ,
-- -- CTE2 as (
-- --     select *,
-- --     SUM(tot_day_amount) OVER(ORDER BY visited_on rows between 6 preceding and current row) as tot_amt
-- --     from CTE
-- -- )

-- -- select visited_on, tot_amt as amount, ROUND(tot_amt/7,2) as average_amount from CTE2 
-- -- where visited_on >= (select DATE_ADD(MIN(visited_on), INTERVAL 6 DAY) from customer)















-- with CTE as (
-- select *, SUM(amount) as tot_amt
-- from customer group by visited_on
-- )
-- select *, 
-- SUM(tot_amt) OVER(ORDER BY visited_on rows between 6 preceding and current row) as rol_amt 
-- from CTE where visited_on >= (select DATE_ADD(MIN(visited_on), INTERVAL 6 DAY) from customer)





with CTE as (
select visited_on, SUM(amount) as tot_amt from Customer group by visited_on
),
CTE2 as (
    select *, 
    SUM(tot_amt) OVER(ORDER BY visited_on rows between 6 preceding and current row) as roll_amt
    from CTE
)
select visited_on, roll_amt as amount, 
ROUND(roll_amt/7,2) as average_amount
from CTE2
where visited_on >= (select distinct(visited_on) from Customer where DATEDIFF(visited_on, (select MIN(visited_on) from Customer)) = 6)
order by visited_on
