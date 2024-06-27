WITH CTE AS (
    SELECT *,DATE_FORMAT(start_date,'%Y-%m') as m, MONTH(start_date) as mm
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE MONTH(start_date) BETWEEN '8' AND '10'
), CTE2 AS (
    SELECT car_id, COUNT(car_id) as c
    FROM CTE
    GROUP BY car_id
), CTE3 AS (
    SELECT c.car_id, m, mm
    FROM CTE c JOIN CTE2 c2
        ON c2.c >=5 AND c2.car_id = c.car_id
)
SELECT mm as MONTH ,car_id as CAR_ID, COUNT(car_id) as RECORDS
FROM CTE3
GROUP BY car_id,m
ORDER BY m, CAR_ID DESC