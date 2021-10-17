
-- 作为计算字段的子查询， 比较慢
SELECT
    employee_id,
    (SELECT
        COUNT(*)
     FROM
        Employee AS E2
     WHERE
        E2.team_id = E1.team_id
    ) AS team_size
FROM
    Employee AS E1


-- ==========================================

SELECT
    employee_id,
    T.freq AS team_size
FROM
    Employee AS E
    JOIN
    (
    SELECT
        team_id, COUNT(*) AS freq
    FROM
        Employee
    GROUP BY
        team_id
    ) AS T
    ON
    E.team_id = T.team_id

-- ==========================================

-- WINDOW FUNCTION

SELECT
    employee_id,
    COUNT(*) OVER(PARTITION BY team_id) AS team_size
FROM
    Employee