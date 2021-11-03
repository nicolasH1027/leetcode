
WITH CTE AS 
(
    SELECT
        order_id,
        AVG(quantity) AS average,
        MAX(quantity) AS maximum
    FROM
        OrdersDetails
    GROUP BY
        order_id
)


SELECT
    order_id
FROM
    CTE
WHERE
    maximum > 
    (
    SELECT
        MAX(average)
    FROM
        CTE
    )
