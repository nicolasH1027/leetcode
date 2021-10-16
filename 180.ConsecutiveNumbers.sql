
SELECT
    DISTINCT L1.Num AS ConsecutiveNums
FROM
    Logs AS L1
    JOIN
    Logs AS L2
    ON
    L1.Id = L2.Id - 1
    JOIN
    Logs AS L3
    ON
    L2.Id = L3.Id - 1
WHERE
    L1.Num = L2.Num
    AND
    L2.Num = L3.Num

-- =======================================================
SELECT
    DISTINCT L1.Num AS ConsecutiveNums
FROM
    Logs AS L1,
    Logs AS L2,
    Logs AS L3
WHERE
    L2.Id = L3.Id - 1
    AND
    L1.Id = L2.Id - 1
    AND
    L1.Num = L2.Num
    AND
    L2.Num = L3.Num
-- =======================================================

SELECT 
    DISTINCT num AS ConsecutiveNums
FROM
    (
    SELECT 
        num,
        LEAD(num) OVER(ORDER BY Id) AS ld, 
        LAG(num) OVER (ORDER BY Id) AS lg
    FROM 
        Logs
    ) T
WHERE 
    num=ld and num=lg;