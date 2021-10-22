
SELECT
    CASE
        WHEN T2.product_id IS NULL THEN T3.product_id
        ELSE T2.product_id
    END AS product_id,
    CASE
        WHEN T2.product_id IS NULL THEN 10
        ELSE T2.new_price
    END AS price
FROM
    (
    SELECT
        DISTINCT product_id
    FROM    
        Products
    ) AS T3
    LEFT JOIN
    (
    SELECT
        product_id, 
        new_price
    FROM
        (
        SELECT
            *,
            RANK() OVER(PARTITION BY product_id ORDER BY change_date DESC) AS rankings
        FROM
            Products
        WHERE
            change_date <= "2019-08-16"
        ) AS T1
    WHERE rankings = 1
    ) AS T2
    ON T3.product_id = T2.product_id


-- ==========================================================================

SELECT
    DISTINCT product_id,
    10 AS price
FROM
    Products
GROUP BY
    product_id
HAVING
    MIN(change_date) > "2019-08-16"
UNION
SELECT
    p2.product_id, new_price
FROM
    Products AS P
WHERE
    (P.product_id, P.change_date) IN
    (
    SELECT
        product_id,
        MAX(change_date) AS recent_date
    FROM
        Products
    WHERE
        change_date <= "2019-08-16"
    GROUP BY
        product_id
    )

