-- with CTE as (
--     select 
--     CASE
--     WHEN income < 20000 THEN "Low Salary"
--     WHEN income >= 20000 and income <= 50000 THEN "Average Salary"
--     ELSE "High Salary" 
--     END 
--     as category
--     from 
--     accounts
-- )

-- select category, COUNT(category)  as accounts_count from CTE group by 1 
-- -- select * from CTE

select 'Low Salary' as category, COUNT(account_id) as accounts_count 
from accounts where income  < 20000
union all
select 'Average Salary' as category, COUNT(account_id) as accounts_count 
from accounts where income  >= 20000 and income <= 50000
union all
select 'High Salary' as category, COUNT(account_id) as accounts_count 
from accounts where income>50000












-- select 
-- CASE 
--     WHEN income < 20000 THEN "Low Salary"
--     WHEN income <= 50000 THEN "Average Salary"
--     ELSE "High Salary"
-- END as category
-- from Accounts