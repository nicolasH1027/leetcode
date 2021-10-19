SELECT
    id,
    'Root' AS Type
FROM
    tree
WHERE
    p_id IS NULL
UNION
SELECT
    id,
    'Leaf' AS Type
FROM
    tree
WHERE
    id NOT IN
    (
    SELECT
        DISTINCT p_id
    FROM
        tree
    WHERE
        p_id IS NOT NULL
    )
    AND
    id <> 
    (
    SELECT
        id
    FROM
        tree
    WHERE
        p_id IS NULL
    )
UNION
SELECT
    id,
    'Inner' AS Type
FROM
    tree
WHERE
    id IN 
    (
    SELECT DISTINCT
        p_id
    FROM
        tree
    WHERE
        p_id IS NOT NULL
    )
    AND 
    p_id IS NOT NULL
ORDER BY
    id


-- ===========================================

SELECT
    id,
    CASE
        WHEN p_id IS NULL THEN 'Root'
        WHEN id in (SELECT DISTINCT p_id FROM tree WHERE p_id IS NOT NULL) THEN 'Inner'
        ELSE 'Leaf'
    END AS Type
FROM
    tree



SELECT
    id,
    IF(p_id IS NULL, 'Root', IF(id in (SELECT DISTINCT p_id FROM tree WHERE p_id IS NOT NULL), 'Inner', 'Leaf')) AS Type
FROM
    tree


-- ===========================================

SELECT
    DISTINCT t1.id,
    CASE
        WHEN t1.p_id IS NULL THEN 'Root'
        WHEN t2.p_id IS NULL THEN 'Leaf'
        ELSE 'Inner'
    END AS Type
FROM
    tree AS t1
    LEFT JOIN
    tree AS t2
    ON
    t1.id = t2.p_id
ORDER BY 1
