SELECT
    customer_id,
    (SELECT customer_name FROM Customers AS C WHERE C.customer_id = O.customer_id) AS customer_name
FROM
    Orders AS O
GROUP BY
    customer_id
HAVING
    SUM(CASE WHEN product_name = 'A' THEN 1 ELSE 0 END) > 0
    AND
    SUM(CASE WHEN product_name = 'B' THEN 1 ELSE 0 END) > 0
    AND
    SUM(CASE WHEN product_name = 'C' THEN 1 ELSE 0 END) = 0




-- =============================================================================

SELECT
    customer_id,
    customer_name
FROM
    Customers
WHERE
    customer_id IN
    (
    SELECT 
        customer_id
    FROM 
        Orders
    WHERE 
        product_name='A'
    ) AND customer_id IN
    (
    SELECT 
        customer_id
    FROM 
        Orders
    WHERE 
        product_name='B'
    ) AND customer_id NOT IN
    (
    SELECT 
        customer_id
    FROM 
        Orders
    WHERE 
        product_name='C'
    )