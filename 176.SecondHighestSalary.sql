
SELECT
    (
    SELECT
        MAX(Salary)
    FROM
        Employee
    WHERE
        Salary <
        (
        SELECT
            MAX(Salary)
        FROM
            Employee
        )
    ) AS SecondHighestSalary 




SELECT MAX(Salary) AS SecondHighestSalary 

FROM Employee 

WHERE Salary < (SELECT MAX(Salary) FROM Employee)


SELECT
    (SELECT 
        DISTINCT Salary
    FROM
        Employee
    ORDER BY 
        Salary DESC
    LIMIT 1 OFFSET 1) 
    AS SecondHighestSalary