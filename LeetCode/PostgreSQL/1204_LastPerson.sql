WITH cte AS
(
    SELECT turn, person_name, weight,
        SUM(Weight) OVER (ORDER BY Turn) AS total_weight
    FROM Queue
),

cte2 AS
(
    SELECT *
    FROM cte
    WHERE total_weight <=1000
)

SELECT person_name
FROM cte2
ORDER BY total_weight DESC
LIMIT 1;