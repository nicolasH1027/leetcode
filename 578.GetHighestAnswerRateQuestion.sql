SELECT
    question_id AS survey_log
FROM
    survey_log
GROUP BY
    question_id
ORDER BY
    AVG(IF(action = 'answer', 1, 0)) DESC
LIMIT 1

-- =========================================================================
SELECT
    question_id AS survey_log
FROM
    (
    SELECT
        question_id,
        AVG(IF(action = 'answer', 1, 0)) AS ratio
    FROM
        survey_log
    GROUP BY
        question_id
    ) AS T
WHERE
    ratio = 
    (
    SELECT
        AVG(IF(action = 'answer', 1, 0)) AS ratio
    FROM
        survey_log
    GROUP BY
        question_id
    ORDER BY
        AVG(IF(action = 'answer', 1, 0)) DESC
    LIMIT 1
    )

-- ===========================================================================

select question_id as 'survey_log'
from(
select question_id, rank() over(order by avg(case when action = 'answer' then 1 else 0 end) desc) r
from survey_log
group by question_id) t
where r=1