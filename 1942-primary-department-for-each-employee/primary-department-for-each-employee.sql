select employee_id, department_id from employee group by 1 having count(employee_id) = 1
union
select employee_id, department_id from employee where employee_id in (
select employee_id from employee group by 1 having count(employee_id) > 1)
and primary_flag = "Y"