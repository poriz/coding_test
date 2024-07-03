WITH HR_GRADE2 AS (
    SELECT EMP_NO, AVG(SCORE) AS SCORE
    FROM HR_GRADE
    GROUP BY EMP_NO,YEAR
)
SELECT g.EMP_NO, e.EMP_NAME,
    CASE 
    WHEN g.score >= 96 THEN 'S'
    WHEN g.score >= 90 THEN 'A'
    WHEN g.score >= 80 THEN 'B'
    ELSE 'C' END AS GRADE,
    CASE 
    WHEN g.score >= 96 THEN e.SAl * 0.2
    WHEN g.score >= 90 THEN e.SAL * 0.15
    WHEN g.score >= 80 THEN e.SAL * 0.1
    ELSE e.SAL * 0 END AS BONUS
    
FROM HR_GRADE2 g JOIN HR_EMPLOYEES e
    ON g.EMP_NO = e.EMP_NO
ORDER BY EMP_NO
