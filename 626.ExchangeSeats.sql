

SELECT
    IF(id < (SELECT COUNT(*) FROM seat), 
      IF(id % 2 = 1, id + 1, id -1),
      IF(id % 2 = 1, id, id - 1)) AS id,
    student
FROM
    seat
ORDER BY
    id

-- ==========================================================

'ROW_NUMBER()'
SELECT
    ROW_NUMBER() OVER() AS id,
    student
FROM
    seat
ORDER BY
    IF(id % 2 = 1, id + 1, id - 1)

