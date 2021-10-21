
SELECT
    MAX(IF(continent = 'America', name, NULL)) AS America,
    MAX(IF(continent = 'Asia', name, NULL)) AS Asia,
    MAX(IF(continent = 'Europe', name, NULL)) AS Europe
FROM
    (
    SELECT
        *,
        ROW_NUMBER() OVER(PARTITION BY continent ORDER BY name) AS ranking
    FROM
        Student
    ) AS T
GROUP BY
    ranking





-- ===========================================================================================

SELECT
    MAX(America) AS America,
    MAX(Asia) AS Asia,
    MAX(Europe) AS Europe
FROM
    (
    SELECT
        CASE
            WHEN continent = 'America' THEN @r1:= @r1 + 1
            WHEN continent = 'Asia' THEN @r2:= @r2 + 1
            WHEN continent = 'Europe' THEN @r3:= @r3 + 1
        END AS ranking,
        CASE
            WHEN continent = 'America' THEN name
        END AS America,
        CASE
            WHEN continent = 'Asia' THEN name
        END AS Asia,
        CASE
            WHEN continent = 'Europe' THEN name
        END AS Europe
    FROM
        Student, (SELECT @r1:=0, @r2:=0, @r3:=0) AS T1
    ORDER BY 
        name
    ) AS T2
GROUP BY
    ranking
