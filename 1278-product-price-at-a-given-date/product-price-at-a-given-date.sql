-- select product_id, 10 as price
-- from products
-- group by 1
-- having MIN(change_date) > '2019-08-16'
-- UNION ALL
-- select product_id, new_price
-- from products 
-- where (product_id, change_date) in (
--     select product_id, MAX(change_date)
--     from products 
--     where change_date <= '2019-08-16'
--     group by 1
-- )









-- -- select product_id, 10 as price from Products 
-- -- group by 1 Having MIN(change_date) > "2019-08-16" 

-- select product_id, price from Products where (product_id, price) in (
--     select product_id, price from Products group 
-- )








-- select product_id, 10 as price from Products 
-- group by 1
-- having MIN(change_date) > "2019-08-16"
-- union
-- select product_id, new_price as price from Products where  
-- (product_id, change_date) in (
--     select product_id, MAX(change_date) from products 
--     where change_date <= "2019-08-16"
--     group by 1
-- )




















select product_id, 10 as price from Products
group by 1
having MIN(change_date) > '2019-08-16'
union
select distinct product_id, new_price as price from Products 
where (product_id, change_date) in (
    select product_id, MAX(change_date) from Products 
    where change_date <= '2019-08-16'
    group by 1
)
