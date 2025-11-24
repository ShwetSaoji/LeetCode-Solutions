# Write your MySQL query statement below
select id, 'Root' as type from Tree
where p_id is NULL
union
select id, 'Inner' as type from Tree
where id in (select distinct p_id from Tree) and p_id is not NULL
union
select id, 'Leaf' as type from Tree
where id not in (select distinct p_id from Tree where p_id is not null)
and p_id is not null

