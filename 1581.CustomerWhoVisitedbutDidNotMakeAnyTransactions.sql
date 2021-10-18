SELECT
    V.customer_id,
    COUNT(*) AS count_no_trans
FROM
    Visits AS V
    LEFT JOIN
    Transactions AS T
    ON
    V.visit_id = T.visit_id
WHERE
    T.transaction_id IS NULL
GROUP BY
    V.customer_id


SELECT 
    customer_id, 
    COUNT(visit_id) as count_no_trans
FROM 
    visits
WHERE 
    visit_id NOT IN (SELECT visit_id FROM transactions)
GROUP BY 
    customer_id