```sql
SELECT
	customerNumber, customerName, country
FROM
	customers
WHERE
	country != 'USA'
ORDER BY
	customerNumber DESC;

-- 문자열 표시 빼먹지 말 것!
```

```sql
SELECT
	YEAR(orderDate) AS year,
    COUNT(orderNumber)
FROM
	orders
GROUP BY
	YEAR(orderDate);

-- YEAR()
```

```sql
SELECT
	productLine, MAX(quantityInStock) AS max_stock
FROM
	products
GROUP BY
	productLine
HAVING
	max_stock < 9000;

-- WHERE와 HAVING 차이
```