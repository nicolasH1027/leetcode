
SELECT
    name,
    mail
FROM
    Contests
    JOIN
    Users
    ON
    gold_medal = user_id
GROUP BY
    gold_medal
HAVING
    COUNT(*) >= 3
  
UNION

SELECT
    name,
    mail
FROM
    Users,
    Contests AS C1,
    Contests AS C2,
    Contests AS C3
WHERE
    user_id IN (C1.gold_medal, C1.silver_medal, C1.bronze_medal)
    AND
    user_id IN (C2.gold_medal, C2.silver_medal, C2.bronze_medal)
    AND
    user_id IN (C3.gold_medal, C3.silver_medal, C3.bronze_medal)
    AND
    C1.contest_id = C2.contest_id - 1
    AND
    C2.contest_id = C3.contest_id - 1

-- =========================================================================

with t0 as (
    select gold_medal as user, contest_id 
    from contests 
    union all 
    select silver_medal as user, contest_id 
    from contests 
    union all 
    select bronze_medal as user, contest_id 
    from contests 
)
, t1 as (
    select user, contest_id, row_number() over(partition by user order by contest_id) as rn 
    from t0 
)
, t2 as (
    select user as user_id -- consecutive medal winners
    from t1 
    group by user, contest_id - rn 
    having count(*) >= 3 -- replace 3 with any number to solve the N problem
    union all
    select gold_medal as user_id  -- gold medal winners
    from contests 
    group by gold_medal 
    having count(*) >= 3
)
select distinct u.name, u.mail 
from t2 
inner join users u
on t2.user_id = u.user_id