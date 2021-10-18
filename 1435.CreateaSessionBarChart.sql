SELECT
    T1.bin,
    IFNULL(COUNT(T2.bin), 0) AS total
FROM
    (
    SELECT
        '[0-5>' AS bin
    UNION
    SELECT
        '[5-10>' AS bin
    UNION    
    SELECT
        '[10-15>' AS bin
    UNION
    SELECT
        '15 or more' AS bin
    ) AS T1
    LEFT JOIN
    (
    SELECT
        *,
        CASE
            WHEN 0 <= duration AND duration < 300 THEN '[0-5>'
            WHEN 300 <= duration AND duration < 600 THEN '[5-10>'
            WHEN 600 <= duration AND duration < 900 THEN '[10-15>'
            ELSE '15 or more'
        END AS bin
    FROM
        Sessions
    ) AS T2
    ON
    T1.bin = T2.bin
GROUP BY
    bin

-- ==================================================================================

SELECT
    '[0-5>' AS bin,
    COUNT(*) AS total
FROM
    Sessions
WHERE
    0 <= duration AND duration < 300
UNION
SELECT
    '[5-10>' AS bin,
    COUNT(*) AS total
FROM
    Sessions
WHERE
    300 <= duration AND duration < 600
UNION
SELECT
    '[10-15>' AS bin,
    COUNT(*) AS total
FROM
    Sessions
WHERE
    600 <= duration AND duration < 900
UNION
SELECT
    '15 or more' AS bin,
    COUNT(*) AS total
FROM
    Sessions
WHERE
    duration >= 900