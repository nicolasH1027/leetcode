SELECT
    product_id,
    'store1' AS store,
    store1 AS price
FROM
    Products
WHERE
    store1 IS NOT NULL
UNION
SELECT
    product_id,
    'store2' AS store,
    store2 AS price
FROM
    Products
WHERE
    store2 IS NOT NULL
UNION
SELECT
    product_id,
    'store3' AS store,
    store3 AS price
FROM
    Products
WHERE
    store3 IS NOT NULL


-- ================================================

SELECT
    *
FROM
    (
    SELECT
        P.product_id,
        T.store,
        CASE
            WHEN T.store = 'store1' THEN P.store1
            WHEN T.store = 'store2' THEN P.store2
            ELSE P.store3
        END AS price
    FROM
        Products AS P
        JOIN
        (
        SELECT 
            'store1' as store
        UNION ALL 
        SELECT 
            'store2' 
        UNION ALL 
        SELECT 
            'store3'
        ) AS T
    ) AS A
WHERE
    A.price IS NOT NULL