
SELECT
    product_id,
    year AS first_year,
    quantity,
    price
FROM
    (
    SELECT
        product_id,
        year,
        quantity,
        price,
        RANK() OVER(PARTITION BY product_id ORDER BY year) AS ranking
    FROM
        Sales    
    ) AS T
WHERE
    ranking = 1

-- ==============================================================================


SELECT 
    product_id, 
    year AS first_year, 
    quantity, 
    price
FROM    
    Sales
WHERE 
    (product_id, year) IN
    (
    SELECT
        product_id, 
        MIN(year) as year
    FROM 
        Sales
    GROUP BY 
        product_id
    )