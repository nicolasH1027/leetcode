SELECT  
    project_id,
    employee_id
FROM
    (
    SELECT
        P.project_id,
        p.employee_id,
        RANK() OVER(PARTITION BY P.project_id ORDER BY E.experience_years DESC) AS ranking
    FROM
        Project AS P
        JOIN
        Employee AS E
        ON
        P.employee_id = E.employee_id
    ) AS T
WHERE
    ranking = 1

-- ==========================================================================================

SELECT 
    p.project_id, 
    e.employee_id
FROM 
    project AS p
    JOIN 
    employee AS e 
    on 
    e.employee_id = p.employee_id
WHERE 
    (p.project_id, e.experience_years) in
    (
    SELECT
        p.project_id, 
        max(e.experience_years)
    FROM 
        project AS p
        JOIN 
        employee AS e 
        on 
        e.employee_id = p.employee_id
    GROUP BY 
        project_id
    )