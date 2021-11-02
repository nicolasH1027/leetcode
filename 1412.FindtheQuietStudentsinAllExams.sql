SELECT
    DISTINCT S.student_id,
    S.student_name
FROM
    Student AS S
    JOIN
    Exam AS E
    ON
    S.student_id = E.student_id
WHERE
    S.student_id NOT IN
(
    SELECT
    student_id
FROM
    (
    SELECT
        E.student_id,
        S.student_name,
        DENSE_RANK() OVER(PARTITION BY E.exam_id ORDER BY E.score) AS ASEC_ORD,
        DENSE_RANK() OVER(PARTITION BY E.exam_id ORDER BY E.score DESC) AS DESC_ORD
    FROM
        Exam AS E
        JOIN
        Student AS S
        ON
        E.student_id = S.student_id
    ) AS T
WHERE
    ASEC_ORD = 1
    OR
    DESC_ORD = 1
)
ORDER BY
    student_id


-- ==============================================================================================

WITH CTE AS 
(
    SELECT
        E.student_id,
        S.student_name,
        DENSE_RANK() OVER(PARTITION BY E.exam_id ORDER BY E.score) AS ASEC_ORD,
        DENSE_RANK() OVER(PARTITION BY E.exam_id ORDER BY E.score DESC) AS DESC_ORD
    FROM
        Exam AS E
        JOIN
        Student AS S
        ON
        E.student_id = S.student_id
)

SELECT
    student_id,
    student_name
FROM
    CTE
WHERE
    student_id NOT IN
    (
        SELECT
            student_id
        FROM
            CTE
        WHERE
            ASEC_ORD = 1
            OR 
            DESC_ORD = 1
    )