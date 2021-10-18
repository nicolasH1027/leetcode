SELECT
    U.name,
    IFNULL(T.dis, 0) AS travelled_distance
FROM
    Users AS U
    LEFT JOIN
    (
    SELECT
        user_id,
        SUM(distance) AS dis
    FROM
        Rides 
    GROUP BY
        user_id   
    ) AS T
    ON
    U.id = T.user_id
ORDER BY
    travelled_distance DESC, U.name

SELECT
    U.name,
    IFNULL(SUM(R.distance), 0) AS travelled_distance
FROM
    Users AS U
    LEFT JOIN
    Rides AS R
    ON 
    U.id = R.user_id
GROUP BY
    U.id
ORDER BY
    travelled_distance DESC,
    U.name