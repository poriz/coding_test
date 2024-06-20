
SELECT i2.item_id, i2.item_name ,i2.rarity
FROM item_info i JOIN item_tree t 
    ON i.item_id = t.parent_item_id
JOIN item_info i2 ON t.item_id = i2.item_id
WHERE i.rarity = 'RARE'
ORDER BY i2.item_id DESC

