SELECT
    DISTINCT ROUND(DIST, 2) AS shortest
FROM
    (
    SELECT
        DIST,
        DENSE_RANK() OVER(ORDER BY DIST) AS ranking
    FROM
        (  
        SELECT
            SQRT(POWER(P1.x - P2.x, 2) + POWER(P1.y - P2.y, 2)) AS DIST
        FROM
            point_2d AS P1
            JOIN
            point_2d AS P2
        ORDER BY
            DIST
        ) AS T1
    ) AS T2
WHERE
    ranking = 2


-- ===========================================================

SELECT
    ROUND(MIN(SQRT(POWER(P1.x - P2.x, 2) + POWER(P1.y - P2.y, 2))), 2) AS shortest
FROM
    point_2d AS P1
    JOIN
    point_2d AS P2
    ON
    P1.x <> P2.x 
    OR
    P1.y <> P2.y

-- ========================================================================

SELECT
    ROUND(MIN(SQRT(POWER(P1.x - P2.x, 2) + POWER(P1.y - P2.y, 2))), 2) AS shortest
FROM
    point_2d AS P1
    JOIN
    point_2d AS P2
    ON
    P1.x < P2.x 
    OR
    (P1.x = P2.x and P1.y < P2.y)