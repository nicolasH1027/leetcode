SELECT
    DISTINCT C1.user_id
FROM
    Confirmations AS C1
    JOIN
    Confirmations AS C2
    ON
    C1.user_id = C2.user_id
    AND
    C1.time_stamp < C2.time_stamp
    AND
    TIMESTAMPDIFF(second, C1.time_stamp, C2.time_stamp) <= 60*60*24