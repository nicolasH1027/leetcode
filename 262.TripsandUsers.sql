
SELECT
    Request_at AS Day,
    ROUND(AVG(IF(Status <> "completed", 1, 0)), 2) AS "Cancellation Rate"
FROM
    trips
WHERE
    Client_Id IN
    (
    SELECT
        Users_Id
    FROM
        Users
    WHERE
        Banned = 'No'
        AND
        Role = 'client'
    )
    AND
    Driver_Id IN
    (
    SELECT
        Users_Id
    FROM
        Users
    WHERE
        Banned = 'No'
        AND
        Role = 'driver'
    )
    AND
    Request_at BETWEEN "2013-10-01" AND "2013-10-03"
GROUP BY
    Request_at


-- ========================================================================


SELECT
    Request_at AS Day,
    ROUND(AVG(IF(Status <> "completed", 1, 0)), 2) AS "Cancellation Rate"
FROM
    trips AS T
    JOIN
    Users AS U1
    ON
    T.Client_ID = U1.Users_Id 
    AND 
    U1.Banned = 'No'
    JOIN
    Users AS U2
    ON
    T.Driver_Id = U2.Users_Id 
    AND
    U2.Banned = 'No'
WHERE
    Request_at BETWEEN "2013-10-01" AND "2013-10-03"
GROUP BY
    Request_at