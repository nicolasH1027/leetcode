SELECT
    DISTINCT LOWER(TRIM(product_name)) AS PRODUCT_NAME,
    DATE_FORMAT(sale_date,"%Y-%m") AS SALE_DATE,
    COUNT(*) AS TOTAL
FROM 
    Sales 
GROUP BY
    1, 2
ORDER BY
    1,2