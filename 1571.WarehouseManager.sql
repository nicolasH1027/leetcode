SELECT
    W.name AS warehouse_name,
    SUM(W.units * P.Width * P.Length * P.Height) AS volume
FROM
    Warehouse AS W
    JOIN
    Products AS P
    ON
    W.product_id = P.product_id
GROUP BY
    W.name

SELECT
    DISTINCT W.name AS warehouse_name,
    SUM(W.units * P.Width * P.Length * P.Height) OVER(PARTITION BY W.name) AS volume
FROM
    Warehouse AS W
    JOIN
    Products AS P
    ON
    W.product_id = P.product_id   
    