-- #1
SELECT
	*
FROM
	employees;

-- #2
SELECT
	customerNumber,
    customerName,
    phone
FROM
	customers;

-- #3
SELECT
	firstName,
    lastName,
    email
FROM
	employees
ORDER BY
	firstName;

-- #4
SELECT
	firstName AS '이름',
    lastName AS '성',
    email AS '이메일'
FROM
	employees
ORDER BY
	이름;

-- #5
SELECT
	employeeNumber,
    lastName,
    firstName,
    officeCode,
    jobTitle
FROM
	employees
ORDER BY
	jobTitle DESC,
    officeCode DESC;

-- #6
SELECT
	*
FROM
	orderdetails
ORDER BY
	quantityOrdered,
    priceEach;
    
-- #7
SELECT
	customerNumber,
    country,
    contactFirstName
FROM
	customers
ORDER BY
	country,
    contactFirstName DESC;
    
-- #8
SELECT
	productCode,
    quantityInStock,
    buyPrice,
    quantityInStock * buyPrice
FROM
	products
ORDER BY
	quantityInStock * buyPrice DESC;

