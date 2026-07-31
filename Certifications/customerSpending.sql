-- Intermediate 2. Customer Spending

/*
Enter your query below.
Please append a semicolon ";" at the end of the query
*/

SELECT c.customer_name,
       CAST(SUM(i.total_price) AS DECIMAL(20,6)) AS amount_spent
FROM customer c
JOIN invoice i ON i.customer_id = c.id
GROUP BY c.id, c.customer_name
HAVING SUM(i.total_price) <= 0.25 * (SELECT AVG(total_price) FROM invoice)
ORDER BY amount_spent DESC;
