# Write your MySQL query statement below
select id, 
(
  CASE
    WHEN p_id is NULL THEN 'Root'
    WHEN id in (select distinct p_id from Tree) then 'Inner'
    ELSE 'Leaf'
  END
) as type
from Tree
