SELECT
    ROUND(SUM(TIV_2016), 2) AS TIV_2016
FROM
    insurance
WHERE
   TIV_2015 IN 
   (
    SELECT  
        TIV_2015
    FROM
        insurance
    GROUP BY
        TIV_2015
    HAVING
        COUNT(*) > 1
    )
    AND
    CONCAT(LAT, ',', LON) IN 
    (
    SELECT
        CONCAT(LAT, ',' ,LON)
    FROM
        insurance
    GROUP BY
        LAT, LON
    HAVING
        COUNT(*) < 2
    )

-- ======================================

SELECT
    ROUND(SUM(TIV_2016), 2) AS TIV_2016
FROM
    (
    SELECT
        *,
        COUNT(*) OVER(PARTITION BY TIV_2015) AS PREV,
        COUNT(*) OVER(PARTITION BY LAT, LON) AS LOCAT
    FROM
        insurance
    ) AS T
WHERE
    PREV > 1
    AND
    LOCAT = 1

-- ======================================

"counter intuitive"

select sum(TIV_2016) TIV_2016
from insurance a
where 1 = (select count(*) from insurance b where a.LAT=b.LAT and a.LON=b.LON) 
and 1 < (select count(*) from insurance c where a.TIV_2015=c.TIV_2015) 