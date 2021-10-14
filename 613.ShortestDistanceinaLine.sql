-- # Write your MySQL query statement below
SELECT
    MIN(ABS(p1.x - p2.x)) AS 'shortest'
FROM
    point AS p1
    JOIN
    point AS p2
    ON
    p1.x <> p2.x

-- faster solution 
SELECT
    MIN(p1.x - p2.x) AS 'shortest'
FROM
    point AS p1
    JOIN
    point AS p2
    ON
    p1.x > p2.x


-- advanced solution  

-- windown function

SELECT 
    MIN(distance) AS shortest 
FROM
    (
    SELECT  
        ABS(x- LEAD(x) OVER(ORDER BY x)) AS distance 
    FROM 
        point
    ) tmp



"""
Follow up: for the sorted table

"""

SELECT 
    MIN(ABS(a.x - b.x)) AS shortest
FROM 
    point a, point b
WHERE
     a.id = b.id - 1