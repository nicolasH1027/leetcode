SELECT
    S.Id, COUNT(*) AS Rank
FROM 
    Scores AS S
    JOIN
        (
        SELECT
            DISTINCT Score
        FROM
            Scores
        ) AS T
    on
        S.Score <= T.Score
GROUP BY
    S.Id
ORDER BY
    S.Score


SELECT
    S.Id, COUNT(*) AS Rank
FROM 
    Scores AS S,
    (
    SELECT
        DISTINCT Score
    FROM
        Scores
    ) AS T
WHERE
    S.Score <= T.Score
GROUP BY
    S.Id
ORDER BY
    S.Score