SELECT
    DISTINCT L1.id,
    (SELECT name FROM Accounts AS A WHERE A.id = L1.id) AS name
FROM
    Logins AS L1
    JOIN 
    Logins AS L2
    ON
    L1.id = L2.id
    AND
    DATEDIFF(L1.login_date, L2.login_date) BETWEEN 0 AND 4
GROUP BY
    L1.id, 
    L1.login_date
HAVING 
    COUNT(DISTINCT L2.login_date) = 5

-- ==============================================================================


WITH RECURSIVE rec_t AS
    (
    SELECT 
        id, login_date, 1 AS days 
    FROM Logins 
    UNION ALL
    SELECT 
        l.id, l.login_date, rec_t.days+1 
    FROM rec_t
        JOIN Logins l 
        ON 
        rec_t.id = l.id 
        AND 
        DATE_ADD(rec_t.login_date, INTERVAL 1 DAY) = l.login_date
    )

SELECT 
    * 
FROM 
    Accounts
WHERE 
    id IN
    (
    SELECT 
        DISTINCT id 
    FROM 
        rec_t 
    WHERE 
        days = 5
    )
ORDER BY 
    id