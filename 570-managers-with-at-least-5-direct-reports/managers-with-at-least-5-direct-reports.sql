-- # Write your MySQL query statement below
-- select name from employee where id in (
-- select managerId from employee group by 1 having count(*) >= 5)

















select name from Employee where id in (
select managerId from Employee group by managerId having count(*)>=5)