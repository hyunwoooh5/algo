SELECT a.id FROM Weather a
INNER JOIN Weather b
    ON a.recordDate = b.recordDate + INTERVAL '1 day'
WHERE b.temperature < a.temperature 