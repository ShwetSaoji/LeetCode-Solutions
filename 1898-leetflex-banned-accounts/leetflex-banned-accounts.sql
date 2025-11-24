# Write your MySQL query statement below

select distinct l1.account_id from LogInfo l1
inner join 
LogInfo l2
on l1.account_id = l2.account_id 
and l1.ip_address != l2.ip_address
and l2.login between l1.login and l1.logout