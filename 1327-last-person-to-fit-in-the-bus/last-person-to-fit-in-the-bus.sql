-- with CTE as (
--     select person_name, 
--     SUM(weight) OVER(order by turn) as cum_weight
--     from queue
-- )

-- select person_name from CTE where cum_weight <= 1000
-- order by cum_weight DESC limit 1
















with CTE as (
select person_name, 
SUM(weight) OVER(ORDER BY turn) as tot_weight
from Queue
)

select person_name from CTE where tot_weight <= 1000
order by tot_weight desc 
limit 1
