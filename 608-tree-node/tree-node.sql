# Write your MySQL query statement below



select id, 
CASE
    WHEN p_id is NULL THEN 'Root'
    WHEN id in (select p_id from Tree) THEN 'Inner'
    ELSE 'Leaf'
END as type
from Tree