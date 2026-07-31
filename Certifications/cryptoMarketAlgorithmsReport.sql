-- Advanced 1. Crypto Market Algorithms Report

/*
Enter your query below.
Please append a semicolon ";" at the end of the query
*/

SELECT c.algorithm,
       CAST(COALESCE(SUM(CASE WHEN MID(t.dt, 6, 2) IN ('01','02','03') THEN t.volume END), 0) AS DECIMAL(20,6)) AS Q1,
       CAST(COALESCE(SUM(CASE WHEN MID(t.dt, 6, 2) IN ('04','05','06') THEN t.volume END), 0) AS DECIMAL(20,6)) AS Q2,
       CAST(COALESCE(SUM(CASE WHEN MID(t.dt, 6, 2) IN ('07','08','09') THEN t.volume END), 0) AS DECIMAL(20,6)) AS Q3,
       CAST(COALESCE(SUM(CASE WHEN MID(t.dt, 6, 2) IN ('10','11','12') THEN t.volume END), 0) AS DECIMAL(20,6)) AS Q4
FROM coins c
JOIN transactions t ON t.coin_code = c.code
WHERE LEFT(t.dt, 4) = '2020'
GROUP BY c.algorithm
ORDER BY c.algorithm ASC;
