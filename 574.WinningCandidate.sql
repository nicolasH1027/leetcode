SELECT
    C.Name
FROM
    Candidate AS C
    JOIN
    (
    SELECT
        CandidateId,
        COUNT(*) AS num
    FROM
        Vote
    GROUP BY
        CandidateId
    ORDER BY 2 DESC
    LIMIT 1
    ) AS T
    ON
    C.id = T.CandidateId

-- ==============================================

"Works for tie case"
SELECT
    C.Name
FROM
    Candidate AS C
    JOIN
    (
    SELECT
        CandidateId,
        RANK() OVER(ORDER BY COUNT(*) DESC) AS ranking
    FROM
        Vote
    GROUP BY
        CandidateId
    ) AS T
    ON 
    C.id = T.CandidateId
WHERE
    ranking = 1