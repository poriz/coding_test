SELECT concat(name,'(',substr(Occupation,1,1),')')  as name
FROM OCCUPATIONS
ORDER BY name;

WITH CTE2 AS (
    SELECT  count(*) as c, occupation
    FROM OCCUPATIONS
    GROUP BY Occupation
    ORDER BY 1 
)
, CTE3 AS (
    SELECT CONCAT('There are a total of ',c,' ',lower(occupation),'s.') as name
    FROM CTE2
)
SELECT name
FROM CTE3;
