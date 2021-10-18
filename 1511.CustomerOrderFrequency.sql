SELECT
    customer_id,
    name
FROM
    (
    SELECT
        C.customer_id, C.name,SUM(T.quantity * P.price) AS TOTAL
    FROM
        Customers AS C
        JOIN
        (
        SELECT
            *
        FROM
            Orders
        WHERE
            order_date BETWEEN '2020-06-1' AND '2020-07-31'
        ) AS T
        ON
        C.customer_id = T.customer_id
        JOIN
        Product AS P
        ON
        T.product_id = P.product_id
    GROUP BY
        C.customer_id, MONTH(T.order_date)
    HAVING
        SUM(T.quantity * P.price) >= 100
    ) AS T
GROUP BY
    customer_id, name
HAVING 
    COUNT(*) = 2


-- =================================================================================

SELECT 
    customer_id,
    name
FROM 
    Customers 
    JOIN 
    Orders 
    USING(customer_id) 
    JOIN 
    Product 
    USING(product_id)
GROUP BY 
    customer_id
HAVING 
    SUM(
        IF(MONTH(order_date) = 6, quantity, 0) * price
    ) >= 100 
    AND 
    SUM(
        IF(MONTH(order_date) = 7, quantity, 0) * price
    ) >= 100;