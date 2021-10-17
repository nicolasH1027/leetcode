
SELECT
    C.country_name,
    CASE
        WHEN average <= 15 THEN 'Cold'
        WHEN average >= 25 THEN 'Hot'
        ELSE 'Warm'
    END AS weather_type
FROM
    Countries AS C
    JOIN
    (
    SELECT
        country_id,
        AVG(weather_state) AS average
    FROM
        Weather
    WHERE
        MONTH(day) = 11
    GROUP BY
        country_id
    ) AS T
    ON
    C.country_id = T.country_id