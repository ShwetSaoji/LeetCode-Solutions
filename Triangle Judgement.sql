select x, y, z , 
CASE WHEN x + y > z AND y + z > x AND x + z > y THEN 'Yes' ELSE 'No' End as triangle
from Triangle
