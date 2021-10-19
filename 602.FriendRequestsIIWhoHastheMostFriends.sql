SELECT
    id,
    SUM(num) AS num
FROM
    (
    SELECT
        requester_id  as id,
        COUNT(*) AS num
    FROM
        request_accepted
    GROUP BY
        requester_id
    union all
    SELECT
        accepter_id as id,
        COUNT(*) AS num
    FROM
        request_accepted
    GROUP BY
        accepter_id
    ) AS T1
GROUP BY
    id
ORDER BY 2 DESC
LIMIT 1


-- ==================================================

"for multiple person who has the same largest number "

SELECT
    id,
    num
FROM
    (
    SELECT
        *,
        RANK() OVER(ORDER BY num DESC) AS ranking
    FROM
        (
        SELECT
            id,
            SUM(num) AS num
        FROM
            (
            SELECT
                requester_id  as id,
                COUNT(*) AS num
            FROM
                request_accepted
            GROUP BY
                requester_id
            union all
            SELECT
                accepter_id as id,
                COUNT(*) AS num
            FROM
                request_accepted
            GROUP BY
                accepter_id
            ) AS T1
        GROUP BY
            id
        ) AS T1
    ) AS T2
WHERE
    T2.ranking = 1


-- ======================================================

"better solution"
SELECT
    id,
    COUNT(*) AS num
FROM
    (
    SELECT
        requester_id  as id
    FROM
        request_accepted
    UNION ALL
    SELECT
        accepter_id  as id
    FROM
        request_accepted
    ) AS T
GROUP BY
    id
ORDER BY
    num DESC
LIMIT 1


"FOLLOW UP"

SELECT
    id,
    COUNT(*) AS num
FROM
    (
    SELECT
        requester_id  as id
    FROM
        request_accepted
    UNION ALL
    SELECT
        accepter_id  as id
    FROM
        request_accepted
    ) AS T
GROUP BY
    id
HAVING
    num = 
    (
    SELECT
        COUNT(*) AS num
    FROM
        (
        SELECT
            requester_id  as id
        FROM
            request_accepted
        UNION ALL
        SELECT
            accepter_id  as id
        FROM
            request_accepted
        ) AS T
    GROUP BY
        id
    ORDER BY
        num DESC
    LIMIT 1
    )

