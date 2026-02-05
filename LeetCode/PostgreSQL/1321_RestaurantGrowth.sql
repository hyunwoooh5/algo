WITH cte AS
(
    SELECT 
        visited_on,
        SUM(amount) as sum_daily
    FROM Customer
    GROUP BY visited_on
),

cte2 AS
(
SELECT 
    visited_on,
    SUM(sum_daily) OVER(ORDER BY visited_on RANGE BETWEEN INTERVAL '6 DAY' PRECEDING AND CURRENT ROW) AS amount
FROM cte
ORDER BY visited_on ASC
)

SELECT *,
    ROUND(amount / 7.0, 2) AS average_amount
FROM cte2
WHERE visited_on >= (SELECT MIN(visited_on) FROM Customer) + INTERVAL '6 DAY'