-- select contest_id, 
-- ROUND(count(contest_id)*100/(select count(*) from users),2) as percentage
-- from register
-- group by 1
-- order by 2 desc, 1










select contest_id, ROUND(count(user_id)*100/(select count(*) from Users),2) as percentage
from Register 
group by 1
order by percentage desc, contest_id