WITH max_length AS (
    SELECT CITY,  length(city) AS len, RANK() OVER (ORDER BY length(city) DESC) as rk
    FROM STATION

)
, max_one AS (
    SELECT CITY, len
    FROM max_length
    WHERE rk = 1
    ORDER BY 1
    LIMIT 1
)
, min_length AS (
    SELECT CITY, length(city) AS len, RANK() OVER (ORDER BY length(city)) as rk
    FROM STATION
)
, min_one AS (
    SELECT CITY, len
    FROM min_length
    WHERE rk = 1
    ORDER BY 1
    LIMIT 1
)
SELECT CITY,len
FROM max_one

UNION

SELECT CITY,len
FROM min_one
