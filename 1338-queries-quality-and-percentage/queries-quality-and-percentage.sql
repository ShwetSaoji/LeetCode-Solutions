-- select query_name, 
-- ROUND(AVG(rating/position),2) as quality,
-- ROUND(AVG(if(rating < 3, 1,0))*100,2) as poor_query_percentage
-- from Queries
-- where query_name is not null
-- group by 1








select query_name, ROUND(AVG(rating/position),2) as quality, 
ROUND(SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END)*100/count(query_name),2) as poor_query_percentage
from Queries 
group by 1