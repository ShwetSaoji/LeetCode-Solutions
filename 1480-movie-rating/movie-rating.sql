


(select u.name as results from users u
inner join 
movierating m
on u.user_id = m.user_id 
group by m.user_id
order by count(m.user_id) desc, u.name
limit 1)
union all
(select m.title as results from movies m 
inner join 
movierating mo
on m.movie_id = mo.movie_id 
where created_at like '2020-02%'
group by mo.movie_id
order by AVG(rating) desc, m.title
limit 1)