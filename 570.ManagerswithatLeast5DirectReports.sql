-- # Write your MySQL query statement below

SELECT
    E1.Name
FROM
    Employee AS E1
    JOIN
    Employee AS E2
    ON
    E1.Id = E2.ManagerId
GROUP BY
    E1.Id
HAVING
    COUNT(*) >= 5


-- ===================================


SELECT
    Name
FROM
    Employee
WHERE
    Id IN
    (
    SELECT
        ManagerId
    FROM
        Employee
    GROUP BY
        ManagerId
    HAVING
        COUNT(*) >= 5
    )

-- ==========================================
'faster'
SELECT
    Name
FROM
    Employee AS t1 
    JOIN
    (SELECT
        ManagerId
    FROM
        Employee
    GROUP BY 
        ManagerId
    HAVING 
        COUNT(ManagerId) >= 5
    ) AS t2
    ON t1.Id = t2.ManagerId