-- # Write your MySQL query statement below

WITH first_login AS 
(
    SELECT
    player_id, min(event_date) AS first_login_day
FROM 
    Activity
GROUP BY
    player_id
), 
main AS 
(
SELECT
    a.player_id
FROM 
    Activity AS a
    JOIN
    first_login AS l
    ON 
    a.player_id = l.player_id AND
    a.event_date = l.first_login_day + 1
)
SELECT
    ROUND((SELECT COUNT(player_id) FROM main) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction