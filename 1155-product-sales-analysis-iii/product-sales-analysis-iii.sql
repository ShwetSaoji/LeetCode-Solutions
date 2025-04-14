-- # Write your MySQL query statement below
-- select product_id, year as first_year, quantity, price
-- from sales
-- where (product_id, year) in (
--     select product_id, MIN(year) from sales
--     group by 1
-- )








with CTE as (
    select *, 
    RANK() OVER(PARTITION BY product_id ORDER BY year) as rnk
    from Sales
)

select c.product_id, c.year as first_year, c.quantity, c.price 
from CTE c 
where c.rnk = 1