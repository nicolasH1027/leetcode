-- # Write your MySQL query statement below
-- abs(number of greater or equal to - number smaller or equal to ) <= 1 


SELECT 
    Id, Company, Salary
FROM 
    (
    SELECT 
        *, 
        ROW_NUMBER() OVER(PARTITION BY COMPANY ORDER BY Salary ASC, Id ASC) AS RN_ASC,
        ROW_NUMBER() OVER(PARTITION BY COMPANY ORDER BY Salary DESC, Id DESC) AS RN_DESC
    FROM
        Employee
    ) AS temp
WHERE 
    RN_ASC - RN_DESC BETWEEN - 1 AND 1
ORDER BY 
    Company, Salary;


-- ================================================================================================


SELECT
    Id, Company, Salary
FROM
    (
    SELECT
        *,
        ROW_NUMBER() OVER(PARTITION BY Company ORDER BY Salary) AS ranking,
        COUNT(Id) OVER(PARTITION BY Company) AS Total
    FROM
        Employee
    ) AS T
WHERE
    ranking BETWEEN Total/2. AND Total/2. + 1
