# CASE Statement and Stored Procedures in SQL Server

## 1. CASE Statement

### What is it?

A `CASE` statement adds conditional logic inside a SQL query. It works like `if / elif / else` logic in Python.

Microsoft describes `CASE` as an expression that can be used in places such as `SELECT`, `WHERE`, `ORDER BY`, `HAVING`, `UPDATE`, and other SQL clauses.
Source: Microsoft SQL Server documentation: https://learn.microsoft.com/en-us/sql/t-sql/language-elements/case-transact-sql

### Why use it?

Use `CASE` when you want to:

- create categories from values
- label rows based on conditions
- create business logic inside a query
- make query output easier to understand

### Basic syntax

```sql
CASE
    WHEN condition_1 THEN result_1
    WHEN condition_2 THEN result_2
    ELSE result_3
END

SELECT
    ProductName,
    UnitPrice,
    CASE
        WHEN UnitPrice >= 50 THEN 'Expensive'
        WHEN UnitPrice >= 20 THEN 'Medium'
        ELSE 'Low price'
    END AS PriceCategory
FROM dbo.Products;
```

### Northwind CASE Example
```sql
SELECT
    c.CustomerID,
    c.CompanyName,
    COUNT(o.OrderID) AS NumberOfOrders,
    CASE
        WHEN COUNT(o.OrderID) > 10 THEN 'High value customer'
        WHEN COUNT(o.OrderID) BETWEEN 5 AND 10 THEN 'Regular customer'
        ELSE 'Low activity customer'
    END AS CustomerSegment
FROM dbo.Customers AS c
INNER JOIN dbo.Orders AS o
    ON c.CustomerID = o.CustomerID
GROUP BY
    c.CustomerID,
    c.CompanyName;
```
# 3. Stored Procedures

## What are they?

A stored procedure is a saved SQL program inside the database. It can contain one or more SQL statements and can be executed whenever needed.

Microsoft defines a stored procedure as a group of one or more Transact-SQL statements stored and run in SQL Server.
Source: https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/stored-procedures-database-engine

---

## Why use stored procedures?

Stored procedures are useful because they:

* save reusable SQL logic
* reduce repeated code
* make complex queries easier to run
* can accept parameters
* support better organisation of database logic
* help standardise business calculations

---

## Basic syntax

```sql
CREATE PROCEDURE procedure_name
AS
BEGIN
    SQL statements;
END;
```

### With a parameter

```sql
CREATE PROCEDURE procedure_name
    @parameter_name DATA_TYPE
AS
BEGIN
    SQL statements;
END;
```

Microsoft SQL Server syntax uses `CREATE PROCEDURE` or `CREATE OR ALTER PROCEDURE`.
Source: https://learn.microsoft.com/en-us/sql/t-sql/statements/create-procedure-transact-sql

---

# 4. Simple Stored Procedure Example

```sql
CREATE PROCEDURE dbo.GetAllCustomers
AS
BEGIN
    SELECT
        CustomerID,
        CompanyName,
        City,
        Country
    FROM dbo.Customers;
END;
```

## To run it

```sql
EXEC dbo.GetAllCustomers;
```

---

# 5. Northwind Stored Procedure Example

This stored procedure returns total spend and number of orders for each customer.

```sql
CREATE PROCEDURE dbo.GetCustomerOrderSummary
AS
BEGIN
    SELECT
        c.CustomerID,
        c.CompanyName,
        COUNT(DISTINCT o.OrderID) AS NumberOfOrders,
        ROUND(SUM(od.UnitPrice * od.Quantity * (1 - od.Discount)), 2) AS TotalSpend
    FROM dbo.Customers AS c
    INNER JOIN dbo.Orders AS o
        ON c.CustomerID = o.CustomerID
    INNER JOIN dbo.[Order Details] AS od
        ON o.OrderID = od.OrderID
    GROUP BY
        c.CustomerID,
        c.CompanyName
    ORDER BY
        TotalSpend DESC;
END;
```

## To run it

```sql
EXEC dbo.GetCustomerOrderSummary;
```

---

# 6. Stored Procedure with Parameter

This procedure returns orders for one selected customer.

```sql
CREATE PROCEDURE dbo.GetOrdersByCustomer
    @CustomerID NVARCHAR(5)
AS
BEGIN
    SELECT
        OrderID,
        CustomerID,
        OrderDate,
        ShippedDate
    FROM dbo.Orders
    WHERE CustomerID = @CustomerID;
END;
```

## To run it

```sql
EXEC dbo.GetOrdersByCustomer @CustomerID = 'ALFKI';
```

---

# 7. What is DRY?

DRY means:

**Don’t Repeat Yourself**

It is a software development principle that means the same logic should not be copied and pasted in many places.

For example, if a business repeatedly calculates order value as:

```sql
UnitPrice * Quantity * (1 - Discount)
```

it is better to define that logic once in a stored procedure or view rather than rewriting it in every query.

---

# 8. How Stored Procedures Help with DRY

Stored procedures help with DRY because they store reusable SQL logic in one place.

Instead of writing the same long query every time, users can simply run:

```sql
EXEC dbo.GetCustomerOrderSummary;
```

## Benefits

* less repeated code
* fewer mistakes
* easier maintenance
* consistent business logic
* cleaner SQL workflow

If the calculation changes later, it can be updated once inside the stored procedure instead of changing many separate queries.

### Notes from training
CASE --> IF/ELSE logic
SP --> Store logic to be called again

```sql
SELECT
    ProductName,
    UnitPrice,
    CASE
        WHEN UnitPrice > 50 THEN 'Premium'
        WHEN UnitPrice > 20 THEN 'Mid-Range'
        ELSE 'Budget'
    END AS PriceCategory
FROM Products;
```
```sql
-- Simple case statement use
SELECT
  ProductName,
  UnitPrice,
  CASE
    WHEN UnitPrice > 20 THEN 'Expensive'
    ELSE 'Affordable'
  END AS PriceCategory
FROM Products;
```
### Example syntax:

```sql
CASE
  WHEN condition THEN result
  WHEN condition THEN result
  ELSE result
END
CASE
  WHEN Quantity > 10 THEN 'Large'
  WHEN Quantity > 5 THEN 'Medium'
  ELSE 'Small'
END
```
```sql
SELECT
  ProductName,
  CASE WHEN UnitPrice > 20 THEN 'High' ELSE 'Low' END AS PriceBand
FROM Products;

ORDER BY
  CASE WHEN UnitPrice > 20 THEN 1 ELSE 2 END;

 GROUP BY
 CASE WHEN UnitPrice > 20 THEN 'High' ELSE 'Low' END;
```

DROP PROCEDURE GetAllProducts