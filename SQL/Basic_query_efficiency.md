# Basic SQL Query Performance

## Aims

- Write more efficient queries
- Implement good JOIN statrtegy
- Use indexes when possible

## What makes a query slow?
- Repeated lookups
- Too much data scanned
- Bad/poor Joins
- Not using a limit when applicable
- Not using filtering when applicable/ bad filtering can be a thing
- Be careful with use sub-queries(use when needed, often they can be substitute by JOINS)
- Not implementing DRY
- Not defining indexes
    - particulary on commonly used/accessable tables

** An easy/simple way of putting it**
" More rows touched, more work for SQL to do".

## Super common query performance problems
1. Basic SELECT
Bad:
```sql
SELECT *
FROM Orders;
```
Better:
```SQL
SELECT OrderID, CustomerID, OrderDate
FROM Orders;
```
2. Using `WHERE`
Bad:
```SQL
SELECT OrderID, CustomerID, OrderDate
FROM Orders;
```
Better:
```SQL
SELECT OrderID, CustomerID, OrderDate
FROM Orders
WHERE OrderDate >= '1997-01-01'
AND OrderDate < '1998-01-01';
```
3. Unnecessary DISTINCT
Bad:
```SQL
SELECT DISTINCT CustomerID
FROM Orders;
```





