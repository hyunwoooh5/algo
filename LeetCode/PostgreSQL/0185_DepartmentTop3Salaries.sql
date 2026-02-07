WITH cte AS
(
    SELECT *, DENSE_RANK() OVER (PARTITION BY departmentID ORDER BY salary DESC) AS rank
    FROM Employee
)

SELECT 
    D.name AS "Department",
    E.name AS "Employee",
    E.salary AS "Salary"
FROM cte E
LEFT JOIN Department D
    ON E.departmentId = D.id
WHERE E.rank <=3