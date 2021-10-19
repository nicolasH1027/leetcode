SELECT
    employee_id,
    IF(COUNT(*) = 1, department_id, (SELECT
    department_id  
FROM
    Employee AS E1
WHERE 
    E1.employee_id = E.employee_id
    AND
    primary_flag = 'Y')) AS department_id
FROM
    Employee AS E
GROUP BY
    employee_id

-- ===========================================================

SELECT 
    employee_id, department_id 
FROM 
    Employee
WHERE 
    primary_flag = 'Y'
UNION
SELECT 
    employee_id, department_id 
FROM 
    Employee 
GROUP BY 
    employee_id
HAVING 
    COUNT(employee_id) = 1

-- ===============================================================

SELECT 
    EMPLOYEE_ID,DEPARTMENT_ID
FROM
    (
    SELECT *, COUNT(EMPLOYEE_ID) OVER(PARTITION BY EMPLOYEE_ID) C
    FROM EMPLOYEE
    ) AS T
WHERE 
    C = 1 
    OR 
    PRIMARY_FLAG ='Y'

-- ====================================================================

SELECT 
    employee_id, department_id
FROM 
    (
    select 
        employee_id, department_id, DENSE_RANK() OVER(partition by employee_id order by primary_flag) AS myrank from employee 
    ) AS T
WHERE 
    myrank=1