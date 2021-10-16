
-- 此模板用于求取分组前N大或者前N 小的值
SELECT
    *
FROM
    (
    SELECT
        *,
        DENSE_RANK() OVER (PARTITION BY <要分组的列名> ORDER BY <要排序的列名> desc) AS ranking
    FROM
        <表名>
    ) AS T
WHERE
    ranking <= N;