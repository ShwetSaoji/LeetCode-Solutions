with CTE as (select requester_id as id, count(requester_id) as num from RequestAccepted
group by 1 
union all
select accepter_id as id, count(accepter_id) as num from RequestAccepted
group by 1 )

select id, SUM(num) as num from CTE group by 1
order by 2 desc limit 1