-- select *,
-- CASE WHEN x + y > z AND y + z > x and z + x > y THEN "Yes" ELSE "No" END as triangle
-- from triangle







select x, y, z, 
CASE 
    WHEN x + y <= z THEN "No"
    WHEN x + z <= y THEN "No" 
    WHEN z + y <= x THEN "No"
    ELSE "Yes"
END as triangle
from Triangle








