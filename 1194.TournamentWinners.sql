SELECT
    group_id,
    player_id
FROM
    (SELECT
        *,
        ROW_NUMBER() OVER(PARTITION BY group_id ORDER BY score DESC, player_id) AS ranking
    FROM
        (SELECT P.group_id, P.player_id, TT.score 
        FROM
            Players AS P
        JOIN
        (SELECT
            player_id,
            SUM(score) AS score
        FROM
            (SELECT
                first_player AS player_id,
                SUM(first_score) AS score
            FROM
                Matches
            GROUP BY
                first_player
            UNION ALL
            SELECT
                second_player AS player_id,
                SUM(second_score) AS score
            FROM
                Matches
            GROUP BY
                second_player
            ) AS T
        GROUP BY
            player_id) AS TT
        ON P.player_id = TT.player_id) TTT) AS TTTT
WHERE
    ranking = 1

-- ===================================================================================

SELECT
    group_id,
    player_id
FROM
    (SELECT
        *,
        ROW_NUMBER() OVER(PARTITION BY group_id ORDER BY score DESC, player_id) AS ranking
    FROM
        (SELECT P.group_id, P.player_id, TT.score 
        FROM
            Players AS P
        JOIN
        (SELECT
            player_id,
            SUM(score) AS score
        FROM
            (SELECT
                first_player AS player_id,
                first_score AS score
            FROM
                Matches
            UNION ALL
            SELECT
                second_player AS player_id,
                second_score AS score
            FROM
                Matches
            ) AS T
        GROUP BY
            player_id) AS TT
        ON P.player_id = TT.player_id) TTT) AS TTTT
WHERE
    ranking = 1