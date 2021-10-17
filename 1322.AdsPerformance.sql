SELECT
    ad_id,
    ROUND(
        IFNULL(
            AVG(
                CASE
                    WHEN action = 'Clicked' THEN 1
                    WHEN action = 'Viewed' THEN 0
                    ELSE NULL
                END
            )*100
        , 0)
    , 2) AS ctr
FROM
    Ads
GROUP BY
    ad_id
ORDER BY
    ctr DESC, ad_id