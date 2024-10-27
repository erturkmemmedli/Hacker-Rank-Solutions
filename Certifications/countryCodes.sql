-- 2. Country Codes

SELECT c.customer_id, c.name, CONCAT('+', cc.country_code, c.phone_number) AS phone
FROM customers AS c
JOIN country_codes AS cc
ON c.country = cc.country
ORDER BY c.customer_id
