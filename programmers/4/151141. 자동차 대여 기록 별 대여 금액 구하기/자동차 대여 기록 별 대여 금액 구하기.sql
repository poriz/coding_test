WITH DAILY_FEE_a1 AS (
    SELECT h.HISTORY_ID
        ,h.CAR_ID
        ,c.DAILY_FEE
        ,DATEDIFF(h.END_DATE,h.START_DATE)+1 AS rent_date        
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY h JOIN CAR_RENTAL_COMPANY_CAR c
        ON h.CAR_ID = c.CAR_ID AND c.CAR_TYPE = '트럭'
),
TOTAL_FEE_a1 AS (
    SELECT *
        ,CASE
            WHEN rent_date >= 90 THEN '90일 이상'
            WHEN rent_date >= 30 THEN '30일 이상'
            WHEN rent_date >= 7  THEN '7일 이상'
        ELSE '7일 미만' END AS DURATION_TYPE
    FROM DAILY_FEE_a1
),
TOTAL_FEE_a2 AS (
    SELECT 
        t.HISTORY_ID
        ,t.CAR_ID
        ,t.DAILY_FEE
        ,t.rent_date
        ,COALESCE(p.DISCOUNT_RATE,0) as DISCOUNT_RATE
    FROM TOTAL_FEE_a1 t LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN p
        ON p.CAR_TYPE = '트럭' AND t.DURATION_TYPE = p.DURATION_TYPE
)
SELECT HISTORY_ID, ROUND((DAILY_FEE * rent_date) * ((100-DISCOUNT_RATE)/100),0)AS FEE
FROM TOTAL_FEE_a2
ORDER BY 2 DESC, 1 DESC
