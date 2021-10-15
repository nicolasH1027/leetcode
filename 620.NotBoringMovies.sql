-- # Write your MySQL query statement below
SELECT
    *
FROM
    Cinema
WHERE
    MOD(id, 2) = 1
    AND
    id NOT IN
    (   SELECT
            id
        FROM
            Cinema
        WHERE
            description LIKE '%boring%'
    )
ORDER BY
    rating DESC

SELECT
    *
FROM
    Cinema
WHERE
    MOD(id, 2) = 1
    AND
    id NOT IN
    (   SELECT
            id
        FROM
            Cinema
        WHERE
            description = 'boring'
    )
ORDER BY
    rating DESC

SELECT
    *
FROM
    cinema
WHERE
    MOD(id, 2) = 1 AND  description <> 'boring'
ORDER BY
    rating DESC