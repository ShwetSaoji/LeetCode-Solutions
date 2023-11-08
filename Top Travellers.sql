select u.name, if(ISNULL(SUM(r.distance)),0,SUM(r.distance)) as travelled_distance from Users u
LEFT JOIN
Rides r 
on u.id=r.user_id
group by r.user_id
order by travelled_distance DESC, name
