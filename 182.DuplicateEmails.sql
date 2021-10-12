-- # Write your MySQL query statement below
SELECT 
    Email
FROM (
    SELECT 
        Email, COUNT(Email) AS Num
    FROM 
        Person 
    GROUP BY
        Email
) AS S
WHERE 
    S.Num > 1 

SELECT
    P.Email AS Email
FROM
    Person AS P
GROUP BY
    P.Email
HAVING
    COUNT(P.Email) > 1
