
Table:
searches
Columns:
date STRING date of the search,
search_id INT the unique identifier of each search,
user_id INT the unique identifier of the searcher,
age_group STRING ('<30', '30-50', '50+'),
search_query STRING the text of the search query

Sample Rows:
date | search_id | user_id | age_group | search_query
--------------------------------------------------------------------
'2020-01-01' | 101 | 9991 | '<30' | 'justin bieber'
'2020-01-01' | 102 | 9991 | '<30' | 'menlo park'
'2020-01-01' | 103 | 5555 | '30-50' | 'john'
'2020-01-01' | 104 | 1234 | '50+' | 'funny cats'


Table:
search_results
Columns:
date STRING date of the search action,
search_id INT the unique identifier of each search,
result_id INT the unique identifier of the result,
result_type STRING (page, event, group, person, post, etc.),
clicked BOOLEAN did the user click on the result?

Sample Rows:
date | search_id | result_id | result_type | clicked
--------------------------------------------------------------------
'2020-01-01' | 101 | 1001 | 'page' | TRUE
'2020-01-01' | 101 | 1002 | 'event' | FALSE
'2020-01-01' | 101 | 1003 | 'event' | FALSE
'2020-01-01' | 101 | 1004 | 'group' | FALSE




Over the last 7 days, how many users made more than 10 searches?

You notice that the number of users that clicked on a search result
about a Facebook Event increased 10% week-over-week. How would you
investigate? How do you decide if this is a good thing or a bad thing?

The Events team wants to up-rank Events such that they show up higher
in Search. How would you determine if this is a good idea or not?




-- 1 question 
SELECT
    COUNT(DISTINCT user_id)
FROM
(
    SELECT
        S.user_id
    FROM
        searches AS S
    WHERE
        DATEDIF(CURDATE(), CAST(S.date AS date)) <= 7
    GROUP BY
        S.user_id
    HAVING
        COUNT(*) > 10
) AS T


-- 2 question
-- what % user clicked on a result about an Event

-- The question is ambiguous, if its about the percentage of user that clicked on a result about an Event over total user 

SELECT
    ROUND(
    (
    SELECT
        COUNT(DISTINCT s2.user_id)
    FROM
        search_result AS s1
        JOIN
        searches AS s2
        ON
        s1.search_id = s2.search_id
    WHERE
        s1.clicked = TRUE
        AND
        s1.result_type = 'event'        
    )
    /
    (SELECT
        DISTINCT user_id
    FROM
        searches)*100, 2) AS Percentage

-- =================================================================================

Welcome to Facebook!

This is just a simple shared plaintext pad, with no execution capabilities.
When you know what language you would like to use for your interview,
simply choose it from the dropdown in the top bar.
Enjoy your interview!

table_name: friending
+-----------------+-------------+------------------------------------------+
| column         | data_type | description |
+-----------------+-------------+------------------------------------------+
| sender_id      | BIGINT    | Facebook Id for user sending request |
| receiver_id    | BIGINT    | Facebook Id for user receiving request |
| sent_date      | STRING    | Date when request was sent |
| accepted_date  | STRING    | Date when request was accepted, NULL if not accepted |
| sender_country | STRING    | Facebook Identifier
+---------------+---------------+------------------------------------------+
sender_id  | receiver_id | sent_date  | accepted_date | sender_country
1          | 2           | 2019-09-15 | 2019-09-18    | US
1          | 3           | 2019-10-15 | 2019-10-15    | US
2          | 3           | 2019-10-15 | NULL          | CA

table_name: age
+---------------+---------------+---------------------------+
| column    | data_type | description |
+---------------+---------------+---------------------------+
| userid    | BIGINT    | Facebook Id for user |
| age_group | STRING    | 'under20', '20-40', '40-60', 'over60' |
+---------------+---------------+---------------------------+
SAMPLE ROWS:
userid | age_group
1234   | '20-40'
5678   | '40-60'
9010   | 'under20'


Q1: What is the same day acceptance rate for every day in the last week?

SELECT
    sent_date,
    SUM(IF(sent_date = accepted_date, 1, 0))/COUNT(*) AS rate
FROM
    friending
WHERE
    CAST(sent_date AS DATE) BETWEEN ... AND ...
GROUP BY
    sent_date


Q2: What is the average number of friendship requests sent per user over the past week by age group?

SELECT
    AVG(Age20) AS Age20,
    AVG(Age2040) AS Age2040,
    AVG(Ageunder20) AS Ageunder20,
    AVG(Ageover60) AS Ageover60
FROM
    (
    SELECT
        F.sender_id AS ID,
        SUM(CASE WHEN A.age_group = '20-40' THEN 1 ELSE 0 END) AS Age20,
        SUM(CASE WHEN A.age_group = '40-60' THEN 1 ELSE 0 END) AS Age2040,
        SUM(CASE WHEN A.age_group = 'under20' THEN 1 ELSE 0 END) AS Ageunder20,
        SUM(CASE WHEN A.age_group = 'over60' THEN 1 ELSE 0 END) AS Ageover60
    FROM
        friending AS F
        JOIN 
        age AS A
        ON
        F.sender_id = A.userid
    WHERE
        CAST(sent_date AS DATE) BETWEEN ... AND ...
    GROUP BY
        F.sender_id
    ) AS T



















Product round:
---------
You are a DS on the friending team. The overall number of friend accepts on the platform has gone down by 5% in June. How would you look into this?
---------
We have a suggestion to add more relatives in the friend algorithm. How would you test if this is a good or a bad idea?-