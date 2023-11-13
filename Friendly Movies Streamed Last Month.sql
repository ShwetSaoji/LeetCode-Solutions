# Write your MySQL query statement below
select distinct(c.title) from Content c
join 
TVProgram t
on c.content_id=t.content_id
and t.program_date like '2020-06%'
where c.content_type="Movies"
and c.Kids_content='Y'
