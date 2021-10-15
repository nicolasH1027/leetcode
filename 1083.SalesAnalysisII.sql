-- # Write your MySQL query statement below
SELECT
    DISTINCT buyer_id
FROM
    Sales
WHERE
    buyer_id IN (
        SELECT
            S.buyer_id
        FROM
            Sales AS S
            JOIN
            Product AS P
            ON
            S.product_id = P.product_id
        WHERE
            P.product_name = 'S8'
    ) AND 
    buyer_id NOT IN (
        SELECT
            S.buyer_id
        FROM
            Sales AS S
            JOIN
            Product AS P
            ON
            S.product_id = P.product_id
        WHERE
            P.product_name = 'iPhone'
    )


SELECT
    DISTINCT S.buyer_id
FROM
    Sales AS S
    JOIN
    Product AS P
    ON
    S.product_id = P.product_id
WHERE
    P.product_name = 'S8'
    AND
    S.buyer_id NOT IN 
    (
        SELECT
            S.buyer_id
        FROM
            Sales AS S
            JOIN
            Product AS P
            ON
            S.product_id = P.product_id
        WHERE
            P.product_name = 'iPhone'
    )