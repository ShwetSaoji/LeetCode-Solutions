# Write your MySQL query statement below
with CTE as (
    select transaction_id, 
    RANK() OVER(
        PARTITION BY DATE(day)
        order by amount DESC
    ) as rnk
    from transactions
)

select transaction_id from CTE where rnk = 1 order by 1
