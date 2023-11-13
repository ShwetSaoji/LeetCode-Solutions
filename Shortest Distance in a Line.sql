# Write your MySQL query statement below
select MIN(abs(a.x-b.x)) as shortest
from point a 
join 
point b
on a.x!=b.x
