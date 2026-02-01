WITH ids AS (
SELECT managerID FROM Employee
GROUP BY managerID
HAVING COUNT(managerID)>=5
) 

SELECT name FROM Employee
WHERE id IN (SELECT managerID FROM ids);



SELECT e1.name FROM Employee e1
JOIN Employee e2
    ON e1.id = e2.managerId
GROUP BY e1.id, e1.name
HAVING COUNT(e2.managerId)>=5;
