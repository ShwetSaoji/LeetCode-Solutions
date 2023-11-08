# Write your MySQL query statement below

select e.left_operand, e.operator, e.right_operand, 
(
   CASE
   WHEN e.operator = '>' and v1.value > v2.value then 'true'
   WHEN e.operator = '<' and v1.value < v2.value then 'true'
   WHEN e.operator = '=' and v1.value = v2.value then 'true'
   ELSE 'false'
   END
) as value
from 
Expressions e
JOIN 
Variables v1 on e.left_operand = v1.name
JOIN 
Variables v2 on e.right_operand = v2.name
