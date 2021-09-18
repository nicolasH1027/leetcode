-- Write your MySQL query statement below
SELECT
    a2.player_id AS player_id,
    a2.event_date AS event_date,
    SUM(games_played) AS games_played_so_far 
FROM 
    Activity AS a1 
    JOIN
    Activity AS a2
    on
    a1.event_date <= a2.event_date AND
    a1.player_id = a2.player_id
GROUP BY
    a2.player_id, a2.event_date
