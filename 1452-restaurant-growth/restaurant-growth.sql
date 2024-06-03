
with CTE as (
    select *, 
    SUM(amount) as tot_day_amount
    from customer 
    group by visited_on
)
,
CTE2 as (
    select *,
    SUM(tot_day_amount) OVER(ORDER BY visited_on rows between 6 preceding and current row) as tot_amt
    from CTE
)

select visited_on, tot_amt as amount, ROUND(tot_amt/7,2) as average_amount from CTE2 
where visited_on >= (select DATE_ADD(MIN(visited_on), INTERVAL 6 DAY) from customer)