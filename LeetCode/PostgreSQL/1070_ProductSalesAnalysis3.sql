WITH cte AS
(
    SELECT product_id, MIN(year) as first_year
    FROM Sales
    GROUP BY product_id
)

SELECT Sales.product_id,
    year AS first_year, quantity, price
FROM Sales
INNER JOIN cte
    ON Sales.product_id = cte.product_id AND Sales.year = cte.first_year