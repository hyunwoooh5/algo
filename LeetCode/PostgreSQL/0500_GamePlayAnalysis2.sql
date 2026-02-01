WITH cte AS
(
    SELECT player_id, MIN(event_date) AS event_date
    FROM Activity
    GROUP BY player_id
)

SELECT ROUND(COUNT(DISTINCT cte.player_id)::numeric/COUNT(DISTINCT Activity.player_id),2) AS fraction
FROM Activity
LEFT JOIN cte
    ON Activity.player_id = cte.player_id AND Activity.event_date = cte.event_date + INTERVAL '1 day'