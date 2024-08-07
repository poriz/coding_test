WITH CTE AS (
    SELECT ID, CART_ID, GROUP_CONCAT(NAME) as products
    FROM CART_PRODUCTS
    GROUP BY CART_ID
)
SELECT CART_ID
FROM CTE
WHERE products like '%Yogurt%' AND products LIKE '%Milk%'
ORDER BY CART_ID