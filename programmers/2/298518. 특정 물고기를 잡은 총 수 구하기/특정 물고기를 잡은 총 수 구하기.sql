SELECT COUNT(*) AS FISH_COUNT
FROM FISH_INFO f JOIN FISH_NAME_INFO i
    ON f.fish_type = i.fish_type
WHERE i.fish_name = 'BASS' OR i.fish_name = 'SNAPPER'