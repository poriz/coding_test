-- 코드를 입력하세요
WITH CTE AS (
    SELECT 
        CASE
        WHEN PRICE/10000 < 1 THEN 0
        ELSE FLOOR(PRICE/10000)*10000 END AS PRICE
    FROM PRODUCT
)
SELECT PRICE AS PRICE_GROUP, COUNT(PRICE) AS PRODUCTS
FROM CTE
GROUP BY PRICE
ORDER BY 1

