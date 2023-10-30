# Write your MySQL query statement below

select 
(CASE 
WHEN
MOD(id,2) != 0 and counts != id THEN id + 1
WHEN
MOD(id,2) != 0 and counts = id THEN id
ELSE id -1
END) as id,
student
from seat, 
(select count(*) as counts from seat) as aa
order by id
