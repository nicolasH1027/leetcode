-- # Write your MySQL query statement below

SELECT
    ROUND(IFNULL(
        (SELECT
            COUNT(DISTINCT requester_id, accepter_id)
        FROM
            RequestAccepted)/(SELECT
            COUNT(DISTINCT sender_id, send_to_id)
        FROM
            FriendRequest)
    , 0), 2) AS accept_rate;

SELECT
ROUND(
    IFNULL(
    (SELECT COUNT(*) FROM (SELECT DISTINCT requester_id, accepter_id FROM RequestAccepted) AS A)
    /
    (SELECT COUNT(*) FROM (SELECT DISTINCT sender_id, send_to_id FROM FriendRequest) AS B),
    0)
, 2) AS accept_rate;


"""follow up questions
Could you write a query to return the acceptance rate for every month?
Could you write a query to return the cumulative acceptance rate for every day?"""


"For the first one"


-- SELECT count(DISTINCT sender_id, send_to_id) AS num, MONTH(request_date) AS month

-- FROM FriendRequest

-- GROUP BY

-- MONTH(request_date)


-- SELECT count(DISTINCT requester_id, accepter_id) AS num, MONTH(accept_date) AS month

-- FROM RequestAccepted

-- GROUP BY

-- MONTH(accept_date)

SELECT
    ROUND(IFNULL(A.num / T.num, 0), 2) AS accept_rate, T.month
FROM
    (
        SELECT 
            count(DISTINCT sender_id, send_to_id) AS num, MONTH(request_date) AS month
        FROM 
            FriendRequest
        GROUP BY
            MONTH(request_date)
    ) AS T
    JOIN
    (
        SELECT 
            count(DISTINCT requester_id, accepter_id) AS num, MONTH(accept_date) AS month
        FROM 
            RequestAccepted
        GROUP BY
            MONTH(accept_date)
    ) AS A
    ON
    T.month = A.month



"For the second one"

SELECT
    ROUND(IFNULL(COUNT(DISTINCT A.requester_id, A.accepter_id) / COUNT(DISTINCT T.sender_id, T.send_to_id),0),2)
FROM 
    FriendRequest AS T,
    RequestAccepted AS A,
    (
        SELECT
            DISTINCT request_date AS date
        FROM
            FriendRequest
        UNION
        SELECT
            DISTINCT accept_date AS date
        FROM 
            RequestAccepted
    ) AS D
WHERE
    A.accept_date <= D.date AND T.request_date <= D.date
GROUP BY
    D.date
ORDER BY
    D.date