select contest_id, 
ROUND(count(contest_id)*100/(select count(*) from users),2) as percentage
from register
group by 1
order by 2 desc, 1