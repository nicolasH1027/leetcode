SELECT
    T1.pay_month,
    T2.department_id,
    CASE
        WHEN T1.average < T2.average THEN 'higher'
        WHEN T1.average > T2.average THEN 'lower'
        ELSE 'same'
    END AS comparison
FROM
    (
    SELECT
        DATE_FORMAT(pay_date, "%Y-%m") AS 'pay_month',
        AVG(amount) AS average
    FROM
        salary
    GROUP BY
        DATE_FORMAT(pay_date, "%Y-%m")
    ) AS T1
    JOIN
    (
    SELECT
        DATE_FORMAT(pay_date, "%Y-%m") AS 'pay_month',
        E.department_id,
        AVG(amount) AS average
    FROM
        salary AS S
        JOIN
        employee AS E
        ON
        S.employee_id = E.employee_id
    GROUP BY
        DATE_FORMAT(pay_date, "%Y-%m"), E.department_id
    ) AS T2
    ON 
    T1.pay_month = T2.pay_month

-- ========================================================================
SELECT
    DISTINCT T.department_id,
    pay_month,
    CASE
        WHEN AVG_COMP < AVG_DEPART THEN 'higher'
        WHEN AVG_COMP > AVG_DEPART THEN 'lower' 
        ELSE 'same'
    END AS comparison
FROM
(
SELECT
    E.department_id, 
    DATE_FORMAT(pay_date, "%Y-%m") AS pay_month,
    AVG(amount) OVER(PARTITION BY DATE_FORMAT(pay_date, "%Y-%m"))  AS AVG_COMP,
    AVG(amount) OVER(PARTITION BY E.department_id, DATE_FORMAT(pay_date, "%Y-%m"))  AS AVG_DEPART 
FROM
    salary AS S
    JOIN
    employee AS E
    ON
    S.employee_id = E.employee_id
) AS T
























