WITH cte AS
(
    SELECT COUNT(product_key) AS num FROM Product
)

SELECT customer_id FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT num FROM cte);