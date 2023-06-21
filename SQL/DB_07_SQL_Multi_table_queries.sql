-- 문제 1
SELECT
	employeeNumber, lastName, firstName, city
FROM
	employees
INNER JOIN offices
	ON	employees.officeCode = offices.officeCode
ORDER BY
	employeeNumber;

-- 문제 2
SELECT
	customerNumber, officeCode, customers.city, offices.city
FROM
	customers
LEFT JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;

-- 문제 3
SELECT
	customerNumber, officeCode, customers.city, offices.city
FROM
	customers
RIGHT JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;

-- 문제 4
SELECT
	customerNumber, officeCode, customers.city, offices.city
FROM
	customers
INNER JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;

-- 문제 5
/*
문제 2: 'LEFT JOIN'을 사용한 쿼리문으로 offices 테이블에서 city 필드 값이 일치하는 레코드와 함께 customers 테이블 전체를 가져온다.
문제 3: 'RIGHT JOIN'을 사용한 쿼리문으로 customers 테이블에서 city 필드 값이 일치하는 레코드와 함께 offices 테이블 전체를 가져온다.
문제 4: 'INNER JOIN'을 사용한 쿼리문으로 customers 테이블과 offices 테이블에서 city 필드 값이 일치하는 레코드만 가져온다.
*/

-- 문제 6
SELECT
	customerNumber, officeCode, customers.city, offices.city
FROM
	customers
LEFT JOIN offices
	ON customers.city = offices.city
UNION
SELECT
	customerNumber, officeCode, customers.city, offices.city
FROM
	customers
RIGHT JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;

-- 문제 7
SELECT
	orderdetails.orderNumber, orderDate
FROM
	orderdetails
INNER JOIN orders
	ON orderdetails.orderNumber = orders.orderNumber
ORDER BY
	orderNumber;

-- 문제 8
SELECT
	orderNumber, orderdetails.productCode, productName
FROM
	orderdetails
INNER JOIN products
	ON orderdetails.productCode = products.productCode
ORDER BY
	orderNumber;

-- 문제 9
SELECT
	orderdetails.orderNumber, orderdetails.productCode, orderDate, productName
FROM
	orderdetails
INNER JOIN orders
	ON orderdetails.orderNumber = orders.orderNumber
INNER JOIN products
	ON orderdetails.productCode = products.productCode
ORDER BY
	orderNumber;