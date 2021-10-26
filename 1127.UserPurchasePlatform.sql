


SELECT
    T1.spend_date,
    T1.platform,
    IFNULL(SUM(T2.total_amount), 0) AS total_amount,
    COUNT(T2.user_id) AS total_users
FROM
(
SELECT
    Distinct spend_date, 'mobile' AS platform 
FROM    
    Spending
UNION
SELECT
    Distinct spend_date, 'desktop' AS platform 
FROM    
    Spending
UNION
SELECT
    Distinct spend_date, 'both' AS platform 
FROM    
    Spending
) AS T1
LEFT JOIN
(
SELECT
    spend_date,
    user_id,
    IF(mobil > 0, IF(desktop > 0, 'both', 'mobile'), 'desktop') AS platform,
    mobil + desktop AS total_amount
FROM
(
SELECT
    spend_date,
    user_id,
    SUM(IF(platform = 'mobile', amount, 0)) AS 'mobil',
    SUM(IF(platform = 'desktop', amount, 0)) AS 'desktop'
FROM    
    Spending
GROUP BY
    spend_date, user_id
) AS T
) AS T2
ON
T1.spend_date = T2.spend_date
AND
T1.platform = T2.platform
GROUP BY
    T1.spend_date, T1.platform