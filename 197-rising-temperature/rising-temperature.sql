# Write your MySQL query statement below

-- with CTE as (
-- select *, 
-- LAG(temperature) OVER(ORDER BY recordDate) as prev_temp
-- from Weather)

-- select id from CTE where temperature > prev_temp

select w1.id from weather w1
inner join weather w2 
on w1.temperature > w2.temperature 
and DATEDIFF(w1.recordDate, w2.recordDate) = 1