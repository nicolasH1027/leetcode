-- # Write your MySQL query statement below
SELECT
    W1.Id
FROM 
    Weather AS W1
    JOIN
    Weather AS W2
WHERE
    W1.Temperature > W2.Temperature
    AND
    DATEDIFF(W1.RecordDate, W2.RecordDate) = 1
