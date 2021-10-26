SELECT
    E1.Id,
    E1.Month,
    SUM(E2.Salary) AS Salary
FROM
    Employee AS E1
    JOIN
    Employee AS E2
    ON
    E1.Id = E2.Id
    AND
    E2.Month BETWEEN E1.Month - 2 AND E1.Month
WHERE
    (E1.Id, E1.Month) NOT IN
    (
    SELECT
        Id, MAX(Month)
    FROM
        Employee
    GROUP BY
        Id
    )
GROUP BY
    E1.Id, E1.Month
ORDER BY
    1, 2 DESC

