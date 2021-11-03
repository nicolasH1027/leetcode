WITH RECURSIVE CTE AS
(
    SELECT
        COUNT(T.transaction_date) AS NUMS
    FROM
        Visits AS V
        LEFT JOIN
        Transactions AS T
        ON
        V.user_id = T.user_id
        AND
        V.visit_date = T.transaction_date
    GROUP BY
        V.user_id, V.visit_date
), CTE2 AS
(
    SELECT 
        0 AS n,
        MAX(NUMS) AS bound
    FROM
        CTE
    UNION ALL
    SELECT
        n + 1,
        bound
    FROM
        CTE2
    WHERE
        n < bound
)

SELECT
    C.n AS transactions_count,
    IFNULL(T.visits_count, 0) AS visits_count
FROM
    CTE2 AS C
    LEFT JOIN
    (
        SELECT
            NUMS AS transactions_count,
            COUNT(*) AS visits_count
        FROM
            CTE
        GROUP BY 
            NUMS
    ) AS T
    ON
    C.n = T.transactions_count
ORDER BY 1