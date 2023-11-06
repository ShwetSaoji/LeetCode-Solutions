with a as 
(
    select requester_id id from RequestAccepted
    UNION ALL
    select accepter_id id from RequestAccepted
)

select id, count(*) num from a group by 1 order by 2 desc limit 1
