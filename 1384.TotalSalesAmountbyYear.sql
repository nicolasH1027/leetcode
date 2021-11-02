WITH RECURSIVE dates AS
(
    SELECT
        MIN(period_start) AS S,
        MAX(period_end) AS E
    FROM
        Sales
    UNION ALL
    SELECT
        DATE_ADD(S, INTERVAL 1 DAY),
        E
    FROM
        dates
    WHERE
        S < E
)


SELECT
    S.product_id,
    P.product_name,
    CAST(YEAR(D.S) AS CHAR) report_year,
    SUM(S.average_daily_sales) AS total_amount
FROM
    Sales AS S
    LEFT JOIN
    Product AS P
    ON
    S.product_id = P.product_id
    LEFT JOIN
    dates AS D
    ON
    D.S BETWEEN S.period_start AND S.period_end
GROUP BY
    S.product_id, P.product_name, YEAR(D.S)
ORDER BY 1, 3