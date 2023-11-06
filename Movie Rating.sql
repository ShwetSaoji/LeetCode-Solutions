(
select u.name as results from users u
inner join 
MovieRating m
on  u.user_id = m.user_id
group by m.user_id
order by COUNT(m.rating) DESC
LIMIT 1
)
UNION ALL
(
select mo.title as results from Movies mo
inner join
MovieRating m
on  mo.movie_id = m.movie_id
where m.created_at like '%2020-02%'
group by m.movie_id
order by AVG(m.rating) DESC, mo.title
LIMIT 1
)
