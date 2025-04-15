-- # Write your MySQL query statement below
-- with CTE as (
--     select *,
--     LAG (id) OVER (order by id) as prev,
--     LEAD (id) OVER (order by id) as next
--     from seat
-- )

-- select if (id%2 = 0, prev, if (next is null, id, next)) as id,
-- student from CTE
-- order by 1











with CTE as (
select *, 
LAG(student) OVER(ORDER BY id) as prev,
LEAD(student) OVER(ORDER BY id) as nxt
from Seat
)

select id, 
CASE 
WHEN id%2<>0 and nxt is NULL THEN student
WHEN id%2=0 THEN prev
ELSE nxt
END as student
from CTE







