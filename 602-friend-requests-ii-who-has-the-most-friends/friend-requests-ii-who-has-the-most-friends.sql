-- with CTE as (select requester_id as id, count(requester_id) as num from RequestAccepted
-- group by 1 
-- union all
-- select accepter_id as id, count(accepter_id) as num from RequestAccepted
-- group by 1 )

-- select id, SUM(num) as num from CTE group by 1
-- order by 2 desc limit 1



















with CTE as (
    select requester_id from RequestAccepted
    UNION ALL
    select accepter_id as requester_id from RequestAccepted
)
select requester_id as id, count(*) as num from CTE group by 1 order by count(*) desc limit 1