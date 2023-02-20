-- 1
SELECT
	productCode, productName, MSRP
FROM
	products
WHERE MSRP > (
	SELECT AVG(MSRP)
    FROM products
)
ORDER BY MSRP;

-- 2
SELECT customerNumber, customerName
FROM customers
WHERE customerNumber IN (
	SELECT customerNumber
    FROM orders
    WHERE orderDate BETWEEN DATE_SUB('2003-01-06', INTERVAL 1 DAY)              
                                     AND '2003-03-26')

ORDER BY customerNumber;

-- 3
SELECT productCode, productName, productLine, MSRP
FROM products
WHERE MSRP = (
	SELECT MAX(MSRP)
    FROM products
    WHERE productLine = 'Classic Cars'
);

-- 4
SELECT customerNumber, customerName, country
FROM customers
WHERE country = (
	SELECT country
    FROM customers
    GROUP BY country
    ORDER BY COUNT(country) DESC
    LIMIT 1
);

-- 5
SELECT customers.customerNumber, customerName, COUNT(orderNumber) AS order_count
FROM customers
INNER JOIN orders
	ON customers.customerNumber = orders.customerNumber
GROUP BY orders.customerNumber
HAVING COUNT(orderNumber) = (
	SELECT COUNT(orderNumber)
	FROM orders
	GROUP BY customerNumber
	ORDER BY COUNT(orderNumber) DESC
    LIMIT 1
);

-- 6
SELECT productCode, productName
FROM products
WHERE productCode IN (
	SELECT orderdetails.productCode
    FROM orderdetails
    INNER JOIN orders
		ON orderdetails.orderNumber = orders.orderNumber
    WHERE YEAR(orderDate) = 2004
)
ORDER BY productCode DESC;