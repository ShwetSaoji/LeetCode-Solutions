# Write your MySQL query statement below
-- select 
-- 'Low Salary' as category,
-- SUM(CASE
--     WHEN income < 20000 THEN 1 ELSE 0 
-- END) as 

with CTE as (
select  
CASE
    WHEN income < 20000 THEN 'Low Salary'
    WHEN income >= 20000 and income <= 50000 THEN 'Average Salary'
    ELSE 'High Salary'
END as categories 
from Accounts)

select 'Low Salary' as category, 
SUM(CASE 
    WHEN categories = 'Low Salary' THEN 1 ELSE 0 
END) as accounts_count 
from CTE
UNION ALL
select 'Average Salary' as category, 
SUM(CASE 
    WHEN categories = 'Average Salary' THEN 1 ELSE 0 
END) as accounts_count 
from CTE
UNION ALL
select 'High Salary' as category, 
SUM(CASE 
    WHEN categories = 'High Salary' THEN 1 ELSE 0 
END) as accounts_count 
from CTE