WITH CTE AS (
    SELECT
        *,
        RANK() OVER (PARTITION BY FISH_TYPE ORDER BY LENGTH DESC) AS rk
    FROM FISH_INFO
)
SELECT c.ID,i.fish_name,c.length
FROM CTE AS c JOIN FISH_NAME_INFO as i 
    ON c.fish_type = i.fish_type
WHERE c.rk = 1
ORDER BY c.id