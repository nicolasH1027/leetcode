SELECT
    DISTINCT C.title
FROM
    TVProgram AS T
    JOIN
    Content AS C
    ON
    T.content_id = C.content_id
WHERE
    MONTH(T.program_date) = 6
    AND
    C.Kids_content = 'Y'
    AND
    C.content_type = 'Movies'