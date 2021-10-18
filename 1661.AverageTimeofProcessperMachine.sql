SELECT
    machine_id,
    ROUND(AVG(time), 3) AS processing_time
FROM
    (
    SELECT
        machine_id,
        process_id,
        SUM(IF(activity_type = 'start', -1*timestamp, timestamp)) AS time
    FROM
        Activity
    GROUP BY
        machine_id,
        process_id
    ) AS T
GROUP BY
    machine_id

-- ===========================================================================

SELECT 
    machine_id, 
    ROUND(SUM(CASE WHEN activity_type = "end" THEN timestamp ELSE -timestamp END)/COUNT(DISTINCT process_id), 3) AS processing_time
FROM 
    Activity
GROUP BY 1