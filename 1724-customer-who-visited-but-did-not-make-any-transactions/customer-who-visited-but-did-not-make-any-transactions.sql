-- select v.customer_id, count(*) as count_no_trans 
-- from Visits v 
-- join 
-- Transactions t
-- on v.visit_id = t.visit_id
-- group by v.customer_id

select customer_id, count(*) as count_no_trans from Visits
where
visit_id not in (select distinct(visit_id) from Transactions)
group by customer_id