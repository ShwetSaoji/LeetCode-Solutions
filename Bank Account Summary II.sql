# Write your MySQL query statement below

with CTE as (
select account, SUM(amount) as balance from Transactions 
group by account having SUM(amount) > 10000
)

select u.name, c.balance from 
users u
inner join 
CTE c
on u.account=c.account
