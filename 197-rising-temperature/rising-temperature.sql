-- select w1.id from Weather w1
-- join 
-- Weather w2
-- on w1.id = (w2.id-1) and w1.temperature > w2.temperature

-- with CTE as (
--     select id, temperature, recordDate ,
--     LAG(recordDate) OVER(ORDER BY recordDate) as prev_date,
--     LAG(temperature) OVER(ORDER BY recordDate) as prev_temp
--     from Weather
-- )
-- select id from CTE where temperature > prev_temp and 
-- DATEDIFF(recordDate, prev_date) = 1

select w1.id from Weather w1
join 
Weather w2
on DATEDIFF(w1.recordDate, w2.recordDate) = 1 and
w1.temperature > w2.temperature