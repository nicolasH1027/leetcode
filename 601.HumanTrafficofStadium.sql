SELECT
    DISTINCT V1.*
FROM
    Stadium AS V1
    JOIN
    Stadium AS V2
    JOIN 
    Stadium AS V3
WHERE
    V1.people >= 100
    AND
    V2.people >= 100
    AND
    V3.people >= 100
    AND
    (
    V1.id = V3.id - 1 AND V3.id = V2.id - 1 AND V2.id - V1.id = 2
    OR
    V2.id = V1.id - 1 AND V1.id = V3.id - 1 AND V3.id - V2.id = 2
    OR
    V3.id = V2.id - 1 AND V2.id = V1.id - 1 AND V1.id - V3.id = 2 
    )
ORDER BY
    V1.visit_date

-- We only care about v1, so we dont need to test all those combination,   5, 6, 7.  v1 = 5, v1 =6, v1 = 7