# Write your MySQL query statement below

WITH CTE1 AS (
    SELECT product_id, order_id, order_date, RANK() OVER (PARTITION BY product_id ORDER BY order_date DESC) as rnk
    FROM Orders o
)

SELECT product_name, p.product_id, order_id, order_date
FROM CTE1 c
JOIN Products p
ON c.product_id=p.product_id
WHERE rnk=1
ORDER BY product_name ASC, product_id ASC, order_id ASC
