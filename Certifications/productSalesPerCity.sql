-- Intermediate 1. Product Sales per City

/*
Enter your query below.
Please append a semicolon ";" at the end of the query
*/

SELECT ci.city_name,
       p.product_name,
       ROUND(SUM(ii.line_total_price), 2) AS total_amount
FROM city ci
JOIN customer c      ON c.city_id = ci.id
JOIN invoice i       ON i.customer_id = c.id
JOIN invoice_item ii ON ii.invoice_id = i.id
JOIN product p       ON p.id = ii.product_id
GROUP BY ci.city_name, p.product_name
ORDER BY total_amount DESC, ci.city_name ASC, p.product_name ASC;
