# 풀이 시 GROUP BY b.AUTHOR_ID, b.CATEGORY 부분을 잘 봐야한다.
# 한번에
SELECT b.AUTHOR_ID, a.AUTHOR_NAME, b.CATEGORY, sum(bs.sales* b.price)  as TOTAL_SALES
FROM BOOK_SALES as bs LEFT JOIN BOOK as b
    ON bs.BOOK_ID =  b.BOOK_ID
    LEFT JOIN author as a ON b.AUTHOR_ID = a.AUTHOR_ID
WHERE month(bs.sales_date) = '1' AND YEAR(bs.sales_date) = '2022'
GROUP BY b.AUTHOR_ID, b.CATEGORY
ORDER BY b.author_id, b.category DESC;

# CTE를 사용해서
WITH CTE AS (
    SELECT book_id,month(sales_date) as m, sum(sales) as s
    FROM BOOK_SALES
    WHERE month(sales_date) = 01 AND YEAR(sales_date) = 2022
    GROUP BY month(sales_date),book_id
),CTE2 as (
    SELECT c.book_id, (c.s * b.price) as TOTAL_SALES, b.category, b.author_id
    FROM CTE c JOIN book b ON c.book_id = b.book_id
)
SELECT a.AUTHOR_ID, a.AUTHOR_NAME, c2.CATEGORY, SUM(c2.TOTAL_SALES) as TOTAL_SALES
FROM CTE2 c2 JOIN author a
    ON c2.author_id = a.author_id
GROUP BY  a.author_id,c2.category
ORDER BY a.author_id, c2.category DESC;

