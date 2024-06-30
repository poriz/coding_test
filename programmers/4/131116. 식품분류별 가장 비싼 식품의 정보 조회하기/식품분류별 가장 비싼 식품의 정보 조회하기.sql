-- 코드를 입력하세요
WITH CTE AS (
    SELECT CATEGORY,PRICE,PRODUCT_NAME,
        RANK() OVER(PARTITION BY CATEGORY ORDER BY PRICE DESC) AS rk
    FROM FOOD_PRODUCT
    WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
)
SELECT CATEGORY,PRICE AS MAX_PRICE,PRODUCT_NAME
FROM CTE
WHERE rk = 1
ORDER BY PRICE DESC

# 이렇게 푸는 법도 있음
# with shortlist as (
# SELECT category, max(price) as max_price, product_name
# from food_product
# where category in ('과자','국','김치','식용유')
# group by 1, 3
# order by 2 desc) -- 2차 group by에서 대표값으로 사용하기 위해서

# select *
# from shortlist
# group by 1;
