# Write your MySQL query statement below
with CTE as (
select seat_id,  free,
LAG(free) OVER(ORDER BY seat_id) as prev, 
LEAD(free) OVER(ORDER BY seat_id) as nxt
from Cinema)

select seat_id from CTE where free = 1 and (free = prev or free = nxt) order by seat_id