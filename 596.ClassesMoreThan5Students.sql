-- # Write your MySQL query statement below
SELECT
    class
FROM 
    courses
GROUP BY
    class
HAVING
    COUNT(DISTINCT student) >= 5


SELECT
    class
FROM
    (   
        SELECT 
            class, COUNT(DISTINCT student) AS num
        FROM
            courses
        GROUP BY
            class
    ) AS T
WHERE
    num >= 5