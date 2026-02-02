WITH cte AS
(
    SELECT reports_to, COUNT(reports_to) AS reports_count, ROUND(AVG(age)) AS average_age
    FROM Employees
    WHERE reports_to IS NOT NULL
    GROUP BY reports_to
)

SELECT 
    employee_id, 
    name,
    reports_count,
    average_age
FROM Employees
INNER JOIN cte
    ON Employees.employee_id = cte.reports_to
ORDER BY employee_id