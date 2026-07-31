-- Advanced 2. Crypto Market Transactions Monitoring

/*
Enter your query below.
Please append a semicolon ";" at the end of the query
*/

WITH ordered AS (
    SELECT sender, dt, amount,
           LAG(dt) OVER (PARTITION BY sender ORDER BY dt) AS prev_dt
    FROM transactions
),
flagged AS (
    SELECT sender, dt, amount,
           CASE
               WHEN prev_dt IS NULL
                 OR TIMESTAMPDIFF(SECOND, CAST(prev_dt AS DATETIME), CAST(dt AS DATETIME)) > 3600
               THEN 1 ELSE 0
           END AS is_new_seq
    FROM ordered
),
grouped AS (
    SELECT sender, dt, amount,
           SUM(is_new_seq) OVER (PARTITION BY sender ORDER BY dt
                                 ROWS UNBOUNDED PRECEDING) AS seq_id
    FROM flagged
)
SELECT sender,
       MIN(dt) AS sequence_start,
       MAX(dt) AS sequence_end,
       COUNT(*) AS transactions_count,
       CAST(SUM(amount) AS DECIMAL(20,6)) AS transactions_sum
FROM grouped
GROUP BY sender, seq_id
HAVING COUNT(*) >= 2 AND SUM(amount) >= 150
ORDER BY sender ASC, sequence_start ASC, sequence_end ASC;
