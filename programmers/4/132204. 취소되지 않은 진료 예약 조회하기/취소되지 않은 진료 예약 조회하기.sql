WITH n_APNT AS (
    SELECT APNT_NO, PT_NO, MCDP_CD, MDDR_ID, APNT_YMD
    FROM APPOINTMENT 
    WHERE DATE_FORMAT(APNT_YMD,'%Y-%m-%d') = '2022-04-13' AND APNT_CNCL_YN = 'N'
        AND MCDP_CD = 'CS'
)
SELECT a.APNT_NO,p.PT_NAME,a.PT_NO,a.MCDP_CD,d.DR_NAME,a.APNT_YMD
FROM n_APNT a JOIN DOCTOR d
    ON a.MDDR_ID = d.DR_ID
    JOIN PATIENT p
    ON a.PT_NO = p.PT_NO
ORDER BY 6
