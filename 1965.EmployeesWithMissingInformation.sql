SELECT
    E.employee_id
FROM
    Employees AS E
    LEFT JOIN
    Salaries AS S
    ON
    E.employee_id = S.employee_id
WHERE
    S.employee_id IS NULL
UNION
SELECT
    S.employee_id
FROM
    Salaries AS S
    LEFT JOIN
    Employees AS E
    ON
    E.employee_id = S.employee_id
WHERE
    E.employee_id IS NULL
ORDER BY
    employee_id

-- ============================================

SELECT 
    employee_id 
FROM 
    Employees 
WHERE 
    employee_id 
    NOT IN 
    (
    SELECT 
        employee_id 
    FROM 
        Salaries
    )
UNION 
SELECT
    employee_id 
FROM 
    Salaries 
WHERE 
    employee_id 
    NOT IN 
    (
    SELECT 
        employee_id 
    FROM 
        Employees
    )
ORDER BY 1 

-- =====================================


SELECT
    employee_id
FROM
    (
    SELECT
        employee_id
    FROM
        Employees
    UNION ALL
    SELECT
        employee_id
    FROM
        Salaries
    ) AS T
GROUP BY
    employee_id
HAVING
    COUNT(*) < 2
ORDER BY
    employee_id