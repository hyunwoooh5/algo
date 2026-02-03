WITH LastChange AS
(
    SELECT product_id, MAX(change_date) AS last_date
    FROM Products
    WHERE change_date <= DATE '2019-08-16'
    GROUP BY product_id
),

CurrentPrices AS
(
    SELECT 
        p.product_id,
        p.new_price as price
    FROM Products p
    JOIN LastChange lc
        ON p.product_id = lc.product_id AND p.change_date = lc.last_date
),

AllProducts AS
(
    SELECT DISTINCT product_id FROM products
)

SELECT
    a.product_id,
    COALESCE(c.price, 10) AS Price
FROM AllProducts a
LEFT JOIN CurrentPrices c
    ON a.product_id = c.product_id