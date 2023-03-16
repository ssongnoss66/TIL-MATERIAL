-- #1
SELECT
	employeeNumber,
  lastName,
  firstName,
  city
FROM
	employees
INNER JOIN offices
	ON employees.officeCode = offices.officeCode
ORDER BY
	employeeNumber;

-- #2
SELECT
	customerNumber,
  officeCode,
  t1.city,
  t2.city
FROM
	customers AS t1
LEFT JOIN offices AS t2
	ON t1.city = t2.city
ORDER BY
	customerNumber DESC;
    
-- #3
SELECT
	customerNumber,
  officeCode,
  t1.city,
  t2.city
FROM
	customers AS t1
RIGHT JOIN offices AS t2
	ON t1.city = t2.city
ORDER BY
	customerNumber DESC;

-- #4
SELECT
	customerNumber,
  officeCode,
  t1.city,
  t2.city
FROM
	customers AS t1
INNER JOIN offices AS t2
	ON t1.city = t2.city
ORDER BY
	customerNumber DESC;

-- #5
-- customers 테이블의 customerNumber, city(t1)
-- employees 테이블의 officeCode, city(t2)

-- 2번 ; LEFT JOIN 하여 오른쪽 테이블(INNER JOIN 이하의 테이블, t2, employees)의 일치하는 레코드와 함께 왼쪽 테이블(FROM 이하의 테이블, t1, customers)의 모든 레코드 반환 (customers 테이블에서 가져온 customerNumber, city(t1)에는 NULL 없음)
-- 3번 ; RIGHT JOIN 하여 왼쪽 테이블(FROM 이하의 테이블, t1, customers)의 일치하는 레코드와 함께 오른쪽 테이블(INNER JOIN 이하의 테이블, t2, employees)의 모든 레코드 반환 (employees 테이블에서 가져온 officeCode, city(t2)에는 NULL 없음)
-- 4번 ; 두 테이블에서 값이 일치하는 레코드에 대해서만 결과 반환 (NULL 없음)

-- #6
SELECT
	customerNumber,
  officeCode,
  t1.city,
  t2.city
FROM
	customers AS t1
LEFT JOIN offices AS t2
	ON t1.city = t2.city
UNION
SELECT
	customerNumber,
  officeCode,
  t1.city,
  t2.city
FROM
	customers AS t1
RIGHT JOIN	offices AS t2
	ON t1.city = t2.city
ORDER BY
	customerNumber DESC;

-- #7
SELECT
	t1.orderNumber,
  orderDate
FROM
	orderdetails AS t1
INNER JOIN orders AS t2
	ON t1.orderNumber = t2.orderNumber
ORDER BY
	orderNumber;

-- #8
SELECT
	orderNumber,
  t1.productCode,
  productName
FROM
	orderdetails AS t1
INNER JOIN products AS t2
	ON t1.productCode = t2.productCode
ORDER BY
	orderNumber;

-- #9
SELECT
	t1.orderNumber,
  t1.productCode,
  orderDate,
  productName
FROM
	orderdetails AS t1
INNER JOIN orders AS t2
	ON t1.orderNumber = t2.orderNumber
INNER JOIN products AS t3
	ON t1.productCode = t3.productCode
ORDER BY
	orderNumber;