-- # Write your MySQL query statement below
SELECT
    E.name AS 'name', B.Bonus as 'Bonus'
FROM
    Employee AS E
    LEFT JOIN
    Bonus AS B
    ON
    E.empId = B.empId
WHERE 
    B.Bonus < 1000 AND B.Bonus IS NULL


SELECT
    E.name AS 'name', B.Bonus as 'Bonus'
FROM
    Employee AS E
    LEFT JOIN
    Bonus AS B
    ON
    E.empId = B.empId
WHERE 
    IFNULL(B.Bonus, 0) < 1000