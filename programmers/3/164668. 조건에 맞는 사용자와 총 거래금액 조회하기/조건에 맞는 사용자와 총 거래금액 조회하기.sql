WITH CTE AS (
    SELECT *
    FROM used_goods_board
    WHERE status = 'DONE'
)
,CTE1 AS (SELECT 
    b.writer_id as USER_ID, 
    u.nickname as NICKNAME, 
    SUM(b.price) as TOTAL_SALES
FROM 
    CTE as b JOIN used_goods_user u
    ON b.writer_id = u.user_id
GROUP BY 
    b.writer_id
)
SELECT *
FROM CTE1
WHERE 
    TOTAL_SALES >= 700000
ORDER BY TOTAL_SALES
