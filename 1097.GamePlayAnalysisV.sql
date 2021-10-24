SELECT
    T.event_date AS install_dt,
    COUNT(T.player_id) AS installs,
    ROUND(COUNT(A.player_id)/COUNT(T.player_id),2) AS Day1_retention
FROM
(
SELECT
    player_id,
    MIN(event_date) AS event_date
FROM
    Activity
GROUP BY
    player_id
) AS T
LEFT JOIN
Activity AS A
ON
T.event_date = A.event_date - 1
AND
T.player_id = A.player_id
GROUP BY
T.event_date