-- Write your MySQL query statement below

SELECT FirstName, LastName, City, State 

FROM Person AS P LEFT JOIN Address AS A

ON P.PersonId = A.PersonId