# Write your MySQL query statement below
SELECT
    DISTINCT P.product_id AS product_id,
    P.product_name AS product_name
FROM
    Sales AS S
    JOIN
    Product AS P
    ON
    S.product_id = P.product_id
WHERE
    S.sale_date BETWEEN '2019-01-01' AND '2019-03-31'
    AND
    P.product_id NOT IN
    (
        SELECT
            P.product_id
        FROM
            Sales AS S
        JOIN
            Product AS P
        ON
            S.product_id = P.product_id
        WHERE
            S.sale_date NOT BETWEEN '2019-01-01' AND '2019-03-31'
    )

SELECT 
    p.product_id, p.product_name
FROM                                                   
    product p
JOIN 
    Sales s
ON 
    p.product_id = s.product_id 
GROUP BY 
    s.product_id
HAVING  
    max(s.sale_date) <= '2019-03-31'
    AND 
    MIN(s.sale_date) >='2019-01-01';