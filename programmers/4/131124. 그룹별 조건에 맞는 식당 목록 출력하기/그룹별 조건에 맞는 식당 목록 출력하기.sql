WITH CTE AS (
    SELECT 
        MEMBER_ID,
        REVIEW_TEXT, 
        REVIEW_DATE,
        COUNT(*) OVER (PARTITION BY MEMBER_ID) as c
    FROM REST_REVIEW
), CTE2 AS (
    SELECT *,RANK() OVER (ORDER BY c DESC) as rk
    FROM CTE
)
SELECT m.MEMBER_NAME, c.REVIEW_TEXT, DATE_FORMAT(c.REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE
FROM CTE2 c JOIN MEMBER_PROFILE m
    ON c.MEMBER_ID = m.MEMBER_ID
WHERE rk = 1
ORDER BY 3,2


# SELECT p.MEMBER_NAME, r.REVIEW_TEXT, DATE_FORMAT(r.REVIEW_DATE,'%Y-%m-%d') AS REVIEW_DATE
# FROM MEMBER_PROFILE p JOIN CTE r
#     ON p.MEMBER_ID = r.MEMBER_ID AND r.rk = 1
# ORDER BY 3,2