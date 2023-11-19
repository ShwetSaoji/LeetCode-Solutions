# Write your MySQL query statement below
with CTE_low as (
    select *, 
    RANK() OVER(
        PARTITION BY exam_id
        ORDER BY score
    ) as rnk
    from exam
),
CTE_max as (
    select *, 
    RANK() OVER(
        PARTITION BY exam_id
        ORDER BY score DESC
    ) as rnk
    from exam
)

select * from student where 
student_id not in (
    select distinct student_id from CTE_low where rnk=1
) 
and
student_id not in (
    select distinct student_id from CTE_max where rnk=1
)
and
student_id in (
    select distinct student_id from exam
)
