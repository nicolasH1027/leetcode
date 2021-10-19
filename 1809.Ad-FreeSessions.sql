SELECT
    session_id
FROM
    Playback
WHERE
    session_id NOT IN
    (   
    SELECT
        session_id
    FROM    
        Playback AS P
        JOIN
        Ads AS A
        ON
        P.customer_id = A.customer_id
    WHERE
        A.timestamp BETWEEN start_time AND end_time
    )

-- =========================================================
SELECT
    P.session_id
FROM
    Playback AS P
    LEFT JOIN
    Ads AS A
    ON
    P.customer_id = A.customer_id
    AND
    A.timestamp BETWEEN P.start_time AND P.end_time
WHERE
    A.customer_id IS NULL