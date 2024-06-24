WITH CTE AS (
    SELECT ID,SIZE_OF_COLONY,
        YEAR(DIFFERENTIATION_DATE) AS YEAR,
        MAX(SIZE_OF_COLONY) OVER (PARTITION BY YEAR(DIFFERENTIATION_DATE) ORDER BY SIZE_OF_COLONY DESC) AS max_size
    FROM ECOLI_DATA
)
SELECT YEAR,
    (max_size - size_of_colony) AS YEAR_DEV,
    ID
FROM CTE
ORDER BY YEAR, YEAR_DEV