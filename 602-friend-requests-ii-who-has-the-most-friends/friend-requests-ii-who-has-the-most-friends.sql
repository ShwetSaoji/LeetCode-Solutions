# Write your MySQL query statement below
with CTE as (
select requester_id as id from RequestAccepted
UNION ALL
select accepter_id as id from RequestAccepted)


select id, COUNT(1) as num from CTE 
group by id 
order by num desc 
LIMIT 1