SELECT
    employee_id
FROM
    Employees
WHERE
    salary < 30000
    AND
    manager_id
    NOT IN
    (
SELECT
    employee_id
FROM
    Employees
    )
ORDER BY 1

-- ===================================

SELECT 
    DISTINCT emp.employee_id
FROM   
    employees emp
    LEFT JOIN 
    employees mng
    ON
    emp.manager_id = mng.employee_id
WHERE  
    emp.manager_id IS NOT NULL
    AND 
    emp.salary < 30000
    AND
    mng.employee_id IS NULL
ORDER  BY 
    emp.employee_id 