# Write your MySQL query statement below
SELECT
    s.name AS 'name'
FROM
    salesperson AS s
WHERE
    s.sales_id NOT IN 
    (
        
    SELECT
        o.sales_id
    FROM
        company AS c
        JOIN
        orders AS o
        on
        c.com_id = o .com_id
    WHERE
        c.name = 'RED'
    
    )

"""
Why three join here doesn't work?

cause there are some null value, which will be neglected by the comparison

"""