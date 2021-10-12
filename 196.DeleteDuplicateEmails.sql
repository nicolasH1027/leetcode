-- your MySQL query statement below
DELETE FROM 
    Person AS P
GROUP BY
    P.Email
HAVING
    P.Id <> MIN(P.Id)



DELETE 
FROM
    Person AS P
WHERE
    P.Id 
    NOT IN (
        SELECT 
            Id
        FROM 
            Person AS P
        GROUP BY
            P.Email
        HAVING
            P.Id = MIN(P.Id)
    )

