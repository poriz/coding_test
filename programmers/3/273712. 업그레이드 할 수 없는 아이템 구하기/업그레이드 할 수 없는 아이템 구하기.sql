-- 코드를 작성해주세요
WITH CTE AS (
    SELECT ITEM_ID
    FROM ITEM_TREE
    WHERE item_id 
        not in (
            SELECT DISTINCT(PARENT_ITEM_ID) 
            FROM ITEM_TREE
            WHERE PARENT_ITEM_ID is not null
        )
)
SELECT c.ITEM_ID,i.ITEM_NAME, i.RARITY
FROM CTE c JOIN ITEM_INFO i
    ON c.ITEM_ID = i.ITEM_ID
ORDER BY c.ITEM_ID DESC