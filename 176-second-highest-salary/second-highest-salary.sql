with CTE as (
    select *,
    DENSE_RANK() OVER(order by salary desc) as rnk
    from employee
)


-- select * from CTE
select 
CASE 
    WHEN max(rnk) < 2 THEN NULL
    ELSE salary
END as SecondHighestSalary
 from CTE where rnk = 2