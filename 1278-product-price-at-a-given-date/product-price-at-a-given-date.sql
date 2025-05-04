# Write your MySQL query statement below

select product_id, 10 as price from Products group by product_id having MIN(change_date) > '2019-08-16'
UNION ALL
select product_id, new_price as price from Products where (product_id, change_date) in (
select product_id, MAX(change_date) from Products where 
(product_id, change_date) in (
    select product_id, change_date from Products where change_date <= '2019-08-16'
)
group by product_id)