# Write your MySQL query statement below

# select distinct(a.seat_id) from cinema a
# join
# cinema b
# where abs(a.seat_id-b.seat_id) = 1 
# and
# a.free = 1
# and 
# b.free = 1
# order by 1


with CTE as (
  select seat_id, free, 
  LAG(free) OVER(ORDER BY seat_id) as prev_free,
  LEAD(free) OVER(ORDER BY seat_id) as next_free
  from cinema
)
select seat_id from CTE
where (free = 1 and prev_free = 1) or 
(free = 1 and next_free=1)
order by 1
