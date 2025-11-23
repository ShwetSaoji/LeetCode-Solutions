# Write your MySQL query statement below
# Write your MySQL query statement below
SELECT c.name AS country
FROM Country c
JOIN Person p
ON c.country_code = LEFT(p.phone_number, 3)
JOIN Calls cl
ON p.id = cl.caller_id OR p.id = cl.callee_id
GROUP BY c.name
HAVING AVG(duration) > (SELECT AVG(duration)
                        FROM Calls)