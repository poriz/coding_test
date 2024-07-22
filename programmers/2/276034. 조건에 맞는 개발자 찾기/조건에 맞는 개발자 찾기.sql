WITH SkillFilter AS (
    SELECT ID, EMAIL, FIRST_NAME, LAST_NAME, SKILL_CODE
    FROM DEVELOPERS
    WHERE (SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = 'Python') > 0)
       OR (SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = 'C#') > 0)
)
SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM SkillFilter
ORDER BY ID;
