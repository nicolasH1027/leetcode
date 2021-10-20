
SELECT
    AVG(Number) AS median
FROM
    (
    SELECT
        *,
        SUM(Frequency) OVER(ORDER BY Number) AS Cumfreq,
        SUM(Frequency) OVER()/2 AS Med_loc
    FROM
        Numbers
    ) AS T
WHERE
    Med_loc BETWEEN Cumfreq - Frequency AND Cumfreq


-- =================================================================
"Not easy to come up with"
SELECT 
    AVG(n.Number) AS median
FROM 
    Numbers n
WHERE 
    n.Frequency >= ABS((SELECT SUM(Frequency) FROM Numbers WHERE Number <= n.Number) -
                         (SELECT SUM(Frequency) FROM Numbers WHERE Number >= n.Number))