# Write your MySQL query statement below
with CTE as (
    select * ,
    LEAD(ip_address) OVER(PARTITION BY account_id order by login) as next_ip,
    LEAD(login) OVER(PARTITION BY account_id order by login) as next_log
    from loginfo
)

select distinct(account_id) from CTE where ip_address!=next_ip and logout >= next_log
