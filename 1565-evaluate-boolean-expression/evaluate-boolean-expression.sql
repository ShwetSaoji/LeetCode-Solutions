-- # Write your MySQL query statement below

-- select 
--     left_operand, 
--     operator, 
--     right_operand, 
--     case
--         when operator = '=' then if((v1.value = v2.value)=1, 'true', 'false')
--         when operator = '>' then if((v1.value > v2.value)=1, 'true', 'false')
--         when operator = '<' then if((v1.value < v2.value)=1, 'true', 'false')
--     end as value
-- from expressions as e 
-- join variables as v1
-- on v1.name = left_operand 
-- join variables as v2
-- on v2.name = right_operand 












select e.*, 
CASE 
WHEN e.operator = '=' THEN if((v1.value = v2.value)=1, 'true', 'false') 
WHEN e.operator = '>' THEN if((v1.value > v2.value)=1, 'true', 'false') 
WHEN e.operator = '<' THEN if((v1.value < v2.value)=1, 'true', 'false') 
END as value
from 
Expressions e
inner join 
Variables v1 
on e.left_operand = v1.name 
inner join 
Variables v2 
on e.right_operand = v2.name 