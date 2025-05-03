# Write your MySQL query statement below


-- select u.name, 
-- COUNT(m.user_id) as tot_review 
-- from users u 
-- inner join 
-- MovieRating m 
-- on u.user_id = m.user_id 
-- group by m.user_id

with CTE as (
select mr.*, 
m.title, u.name from 
MovieRating mr 
inner join 
Movies m 
on mr.movie_id = m.movie_id
inner join 
Users u 
on mr.user_id = u.user_id)

select name as results from (
select user_id, name , COUNT(1) as review_cnt from CTE
group by user_id, name
order by review_cnt desc, name
limit 1) A
union all
select title as results from (
select movie_id, title, AVG(rating) as avg_rating from CTE 
where created_at like '2020-02%'
group by 1, 2 
order by avg_rating desc, title 
limit 1 ) B