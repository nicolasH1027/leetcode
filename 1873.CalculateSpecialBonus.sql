"naive way"

SELECT
    *
FROM
    (
    SELECT
        employee_id,
        salary AS bonus
    FROM
        Employees
    WHERE
        employee_id % 2 = 1
        AND
        name NOT LIKE "M%"
    UNION
    SELECT
        employee_id,
        0 AS bonus
    FROM
        Employees
    WHERE
        employee_id % 2 = 0
        OR
        name LIKE "M%"
    ) AS T
ORDER BY
    employee_id

-- =======================================================

SELECT
    employee_id,
    CASE
        WHEN employee_id%2 = 1 AND name NOT LIKE "M%" THEN salary
        ELSE 0
    END AS bonus
FROM
    Employees
ORDER BY
    employee_id