-- 코드를 작성해주세요

SELECT t.ITEM_ID, i.ITEM_NAME
FROM ITEM_TREE t JOIN ITEM_INFO i
    ON t.item_id = i.item_id
WHERE t.PARENT_ITEM_ID is null