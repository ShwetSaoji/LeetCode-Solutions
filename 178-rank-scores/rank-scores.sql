# Write your MySQL query statement below


select score, 
DENSE_RANK() OVER(ORDER by score desc) as 'rank' 
from Scores 