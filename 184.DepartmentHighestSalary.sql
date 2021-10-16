Employee

Department
SELECT
    T.Name AS 'Department',
    E.Name AS 'Employee',
    T.Salary AS 'Salary'
FROM
    Employee AS E
    ,
    (
    SELECT
        E.DepartmentId AS Id, 
        D.Name AS Name, 
        MAX(E.Salary) AS 'Salary'
    FROM 
        Employee AS E
        JOIN
        Department AS D
        ON
        E.DepartmentId = D.Id
    GROUP BY
        D.Name
    ) AS T
WHERE
    E.DepartmentId = T.Id
    AND
    E.Salary = T.Salary



SELECT
    D.Name AS 'Department',
    T.name AS 'Employee',
    T.Salary AS 'Salary'
FROM
    Department AS D,
    (
    SELECT
        name,
        Salary,
        DepartmentId,
        DENSE_RANK() OVER (PARTITION BY DepartmentId ORDER BY Salary desc) AS ranking
    FROM
        Employee
    ) AS T
WHERE
    D.Id = T.DepartmentId
    AND
    ranking = 1;


SELECT
    Department.name AS 'Department',
    Employee.name AS 'Employee',
    Salary
FROM
    Employee
        JOIN
    Department ON Employee.DepartmentId = Department.Id
WHERE
    (Employee.DepartmentId , Salary) IN
    (   SELECT
            DepartmentId, MAX(Salary)
        FROM
            Employee
        GROUP BY DepartmentId
    )
;