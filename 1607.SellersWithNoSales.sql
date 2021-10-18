SELECT
    S.seller_name
FROM
    Seller AS S
    LEFT JOIN
    (
    SELECT
        *
    FROM
        Orders
    WHERE
        YEAR(sale_date) = 2020
    ) AS O
    ON
    S.seller_id = O.seller_id
WHERE
    O.customer_id IS NULL
ORDER BY
    S.seller_name


-- ==============================================================

SELECT 
    seller_name
FROM 
    Seller 
WHERE  
    seller_id 
    NOT IN (
        SELECT 
            DISTINCT seller_id 
        FROM 
            Orders
        WHERE 
            LEFT(sale_date, 4) = '2020'
)
ORDER BY 1