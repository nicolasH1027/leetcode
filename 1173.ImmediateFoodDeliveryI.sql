SELECT
    ROUND
    (
    (    
    SELECT
        COUNT(*)
    FROM
        Delivery
    WHERE
        order_date = customer_pref_delivery_date
    )/ 
    (    
    SELECT
        COUNT(*)
    FROM
        Delivery
    )*100
    , 2) AS immediate_percentage

select round(100 * sum(order_date = customer_pref_delivery_date) / count(*), 2) as immediate_percentage from Delivery;