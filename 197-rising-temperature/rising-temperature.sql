-- with CTE as (
--     select *,
--     LAG(temperature) OVER(ORDER BY recordDate) as prev_temp
--     from weather
-- )
-- select id from CTE where prev_temp < temperature


select w1.id from weather w1
join weather w2
on DATEDIFF(w1.recordDate, w2.recordDate) = 1
and w1.temperature > w2.temperature