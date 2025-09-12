SELECT s.name FROM SalesPerson AS s
WHERE sales_id NOT IN (
    SELECT sales_id FROM Orders
    WHERE com_id = (
        SELECT com_id FROM company
        WHERE name = 'RED'
    
    )


);