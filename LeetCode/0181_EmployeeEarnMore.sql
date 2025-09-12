SELECT a.name AS employee FROM Employee AS a
JOIN employee AS b
    ON a.managerID = b.id
WHERE a.salary > b.salary;