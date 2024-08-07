WITH g1 AS (
    SELECT ID
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL
)
, g2 AS (
    SELECT e.ID
    FROM g1 g JOIN ECOLI_DATA e
    WHERE e.PARENT_ID = g.ID
)
SELECT e.ID
FROM g2 g JOIN ECOLI_DATA e
WHERE e.PARENT_ID = g.ID
ORDER BY 1
