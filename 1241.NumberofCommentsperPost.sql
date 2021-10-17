-- # Write your MySQL query statement below

SELECT
    DISTINCT S.sub_id AS post_id, 
    IFNULL(T.number_of_comments, 0) AS number_of_comments
FROM
    (
    SELECT
        DISTINCT sub_id
    FROM
        Submissions
    WHERE
        parent_id IS NULL
    ) AS S
    LEFT JOIN
    (
    SELECT
        parent_id, COUNT(DISTINCT sub_id) AS number_of_comments
    FROM
        Submissions
    GROUP BY
        parent_id
    ) AS T
    ON
    S.sub_id = T.parent_id
ORDER BY
    post_id

-- ==============================================================================
SELECT
    DISTINCT sub_id AS post_id,
    (SELECT COUNT(DISTINCT sub_id) FROM Submissions S2 WHERE S1.sub_id = S2.parent_id) AS number_of_comments
FROM
    Submissions AS S1
WHERE parent_id IS NULL
ORDER BY sub_id

-- ==============================================================================
SELECT
    S1.sub_id AS post_id,
    COUNT(DISTINCT S2.sub_id) AS number_of_comments
FROM
    Submissions S1
LEFT JOIN
    Submissions S2
ON
    S1.sub_id = S2.parent_id
WHERE S1.parent_id IS NULL
GROUP BY S1.sub_id
-- ==============================================================================