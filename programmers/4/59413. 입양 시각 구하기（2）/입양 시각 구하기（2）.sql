WITH RECURSIVE CTE AS (
    select 0 as HOUR
    UNION ALL
    select HOUR+1 as num
    from CTE
     where HOUR+1 <= 23
),
CTE2 AS (
    SELECT HOUR(DATETIME) AS HOUR , COUNT(ANIMAL_ID) AS COUNT
    FROM ANIMAL_OUTS
    GROUP BY 1
)
select c1.hour, COALESCE(c2.count,0) AS COUNT
FROM CTE2 c2 right JOIN CTE c1
    ON c1.hour = c2.hour