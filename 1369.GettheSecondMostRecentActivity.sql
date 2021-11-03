SELECT
    U.username,
    U.activity,
    TT.startDate,
    TT.endDate
FROM
    (
    SELECT
        username,
        IF(COUNT(*) = 2, MIN(startDate), MAX(startDate)) AS startDate,
        IF(COUNT(*) = 2, MIN(endDate), MAX(endDate)) AS endDate
    FROM
        (
        SELECT
            U1.username,
            U1.startDate,
            U1.endDate
        FROM
            UserActivity AS U1
            JOIN
            UserActivity AS U2
            ON
            U1.startDate <= U2.startDate
            AND
            U1.username = U2.username
        GROUP BY
            U1.username, U1.startDate, U1.endDate
        HAVING
            COUNT(U2.username) <= 2
        ) AS T
    GROUP BY
        username
    ) AS TT
    JOIN
    UserActivity AS U
    ON
    TT.username = U.username
    AND
    TT.startDate = U.startDate

-- ===============================================================================

SELECT
    username, activity, startDate, endDate
FROM
(
    SELECT
        *, 
        COUNT(activity) OVER(PARTITION BY username ) AS cnt,
        ROW_NUMBER() OVER(PARTITION BY username ORDER BY startdate DESC) AS n
    FROM
        UserActivity
) AS T
WHERE
    n = 2 or cnt = 1