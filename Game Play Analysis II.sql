# Write your MySQL query statement below
with CTE as (
    select player_id, device_id , 
    RANK() OVER(
        PARTITION BY 
        player_id
        ORDER BY EVENT_DATE
    ) as rnk
    from activity
)

select player_id, device_id from CTE where rnk = 1
