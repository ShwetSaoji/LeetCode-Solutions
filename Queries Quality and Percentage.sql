select query_name, ROUND(AVG(rating/position),2) as quality, 
ROUND(AVG(if(rating < 3, 1, 0))*100,2) as poor_query_percentage
from Queries
group by query_name
