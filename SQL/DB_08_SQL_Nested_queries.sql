-- 문제 1
SELECT productCode, productName, MSRP
FROM products
WHERE MSRP > (
	SELECT AVG(MSRP)
    FROM products
)
ORDER BY MSRP;

-- 문제 2
SELECT customerNumber, customerName
FROM customers
WHERE customerNumber IN (
	SELECT customerNumber
    FROM orders
    WHERE orderDate BETWEEN '2003-01-06' AND '2003-03-26'
)
ORDER BY customerNumber;

-- 문제 3
SELECT productCode, productName, productLine, MSRP
FROM (
	SELECT *
    FROM products
    WHERE productLine = 'Classic Cars'
    ) AS Sub
ORDER BY MSRP DESC
LIMIT 1;

-- 문제 4
SELECT customerNumber, customerName, country
FROM customers
WHERE country = (
	SELECT country
	FROM customers
	GROUP BY country
	ORDER BY count(*) DESC
	LIMIT 1
)
ORDER BY customerNumber;

-- 문제 5
SELECT customerNumber, customerName, count(customerNumber) AS 'order_count'
FROM customers
INNER JOIN orders USING (customerNumber)
GROUP BY customerNumber
ORDER BY order_count DESC
LIMIT 1;

-- 문제 6
SELECT orderdetails.productCode, productName 
FROM orderdetails
INNER JOIN (
	SELECT *
    FROM orders
    WHERE orderDate LIKE '2004%'
) AS Sub
	ON orderdetails.orderNumber = Sub.orderNumber
INNER JOIN products
	ON orderdetails.productCode = products.productCode
GROUP BY productCode
ORDER BY productCode DESC;