SELECT
    F1.follower,
    COUNT(DISTINCT F2.follower) AS num
FROM
    follow AS F1
    JOIN
    follow AS F2
    ON
    F1.follower = F2.followee
GROUP BY
    F1.follower

-- ============================================
    