SELECT
    T1.student_id,
    T1.student_name,
    T1.subject_name,
    IFNULL(T2.attended_exams,0) AS attended_exams
FROM
    (
    SELECT
        *
    FROM
        Students
        JOIN
        Subjects
    ) AS T1
    LEFT JOIN
    (
    SELECT
        student_id, COUNT(student_id) AS attended_exams, subject_name
    FROM
        Examinations
    GROUP BY
        student_id,subject_name
    ) AS T2
    ON 
    T1.student_id = T2.student_id
    AND
    T1.Subjects = T2.subject_name
ORDER BY
    T1.student_id, T1.subject_name