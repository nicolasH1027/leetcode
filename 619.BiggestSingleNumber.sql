-- # Write your MySQL query statement below

"""
to return Null, we can use another select to wrap the original, then

we can print the null explicitly
"""
SELECT
    (
    SELECT
        num
    FROM
        my_numbers 
    GROUP BY
        num
    HAVING
        COUNT(*) = 1
    ORDER BY
        num DESC
    LIMIT 1 
    ) AS num;

SELECT
    MAX(num) AS num
FROM
    (SELECT
        num
    FROM
        my_numbers
    GROUP BY 
        num
    HAVING 
        COUNT(num) = 1
    ) AS t;