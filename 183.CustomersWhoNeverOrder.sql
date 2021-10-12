-- # Write your MySQL query statement below
SELECT 
    Name AS 'Customers'
FROM 
    Customers AS C
WHERE
    C.Id 
    NOT IN(
        SELECT 
            CustomerId 
        FROM
            Orders
    )


SELECT 
    c.Name as Customers 
FROM
    Customers AS c
    LEFT JOIN Orders AS o ON
    c.Id = o.CustomerId
WHERE
    o.CustomerId is Null