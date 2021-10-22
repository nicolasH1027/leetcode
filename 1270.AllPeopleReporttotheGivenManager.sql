WITH RECURSIVE BFS AS
    (
    SELECT
        employee_id
    FROM
        Employees
    WHERE
        manager_id = 1
        AND
        employee_id <> 1
    UNION ALL
    SELECT
        E.employee_id
    FROM
        Employees AS E
        JOIN
        BFS AS B
        ON
        E.manager_id = B.employee_id
    )

SELECT
    *
FROM
    BFS
OPTION(MAXRECURSION 3)

-- ==================================================================

WITH RECURSIVE BFS AS
    (
    SELECT
        employee_id,
        1 AS LEVEL
    FROM
        Employees
    WHERE
        manager_id = 1
        AND
        employee_id <> 1
    UNION ALL
    SELECT
        E.employee_id,
        B.LEVEL + 1
    FROM
        Employees AS E
        JOIN
        BFS AS B
        ON
        E.manager_id = B.employee_id
    )

SELECT
    employee_id
FROM
    BFS
WHERE
    LEVEL <= 3