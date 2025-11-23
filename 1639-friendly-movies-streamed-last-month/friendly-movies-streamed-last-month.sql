# Write your MySQL query statement below

select distinct(c.title) from TVProgram t 
inner join 
Content c 
on t.content_id = c.content_id 
where t.program_date like '2020-06%' and 
c.kids_content = 'Y' and content_type = 'Movies'