# Write your MySQL query statement below

select ROUND(sum(i.tiv_2016),2) as tiv_2016 from Insurance i
where i.tiv_2015 in 
(
    select  tiv_2015 from Insurance
    group by tiv_2015 having count(*) > 1
)
and (lat, lon)  in 
(
    select lat, lon from insurance
    group by lat, lon having count(*) = 1
)
