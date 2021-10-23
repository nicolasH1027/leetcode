SELECT
    from_id AS person1,
    to_id AS person2,
    SUM(call_count) AS call_count,
    SUM(total_duration) AS total_duration
FROM
    (
    SELECT
        from_id, to_id,
        COUNT(*) AS call_count,
        SUM(duration) AS total_duration
    FROM
        Calls
    WHERE
        from_id < to_id
    GROUP BY
        from_id, to_id
    UNION ALL 
    SELECT
        to_id AS from_id,
        from_id AS to_id,
        COUNT(*) AS call_count,
        SUM(duration) AS total_duration
    FROM
        Calls
    WHERE
        from_id > to_id
    GROUP BY
        from_id, to_id) AS T
GROUP BY
    from_id, to_id

-- ===================================================================

"GROUP BY 中可以使用别名"

SELECT 
    CASE
        WHEN from_id > to_id THEN to_id
        ELSE from_id
    END AS person1,
    CASE
        WHEN from_id > to_id THEN from_id
        ELSE to_id
    END AS person2,
    COUNT(duration) AS call_count,
    SUM(duration) AS total_duration       
FROM 
    Calls
GROUP BY 
    person2, person1