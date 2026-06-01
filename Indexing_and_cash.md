### Indexing research and tasks

Look at the SQL query below:
```sql
SELECT *
FROM Orders
WHERE CustomerID = 'ALFKI';
```
What is the issue here and how could the concept of "indexing" help?
- Star makes search loaded
- Server needs to go through all rows

What is Indexing?
- Indexing in Microsoft SQL Server is a way to make data retrieval faster.
- Instead of scanning every row in a table, SQL Server can quickly locate the needed rows.
- This improves query efficiency in terms of speed and allocated cost

Tasks:
1. Create your first index for the northwind database (Orders table, CustomerID) - see .sql file for execution

2. Run the query example again, is the time to execute faster? - yes

3. Create a second Index (Orders table, CustomerID and OrderDate)

4. Find out to run a cache wipe

5. Run the following query:
SELECT *
FROM Orders
WHERE CustomerID = 'ALFKI'
ORDER BY OrderDate;


6. Table Scan vs Index Seek

Table Scan

A table scan happens when SQL Server reads the entire table row-by-row to find matching data.

Conceptually:

read everything → then filter

Example:

- no index exists,
- or query is inefficient,
- or SQL Server decides scan is cheaper.

Example query:

SELECT *
FROM dbo.Orders
WHERE CustomerID = 'ALFKI';

Without index on CustomerID, SQL Server may scan the whole table.

Why scans are slower

For large tables:

- more disk reads,
- more memory usage,
- slower performance.

Index Seek

An index seek uses an index to jump directly to matching rows.

Conceptually:

-- use lookup structure → jump directly to data

Like:

book index,
dictionary lookup.

With index:
```sql
CREATE INDEX IX_Orders_CustomerID
ON dbo.Orders(CustomerID);
```
the same query can use an Index Seek instead of scanning entire table.

Why seeks are faster:

- fewer reads,
- less data scanned,
- faster filtering,
- better scalability.

Comparison :
Table Scan :
- reads most/all rows
- slower on large tables
- no useful index
- higher IO (input/output) cost

Index Seek:
- reads only needed rows
- faster
- uses index
- lower IO cost

7. Why Query Order Matters with Indexing

### Order matters because SQL Server uses indexes most efficiently when query structure matches the index structure.

Example composite index:

- (CustomerID, OrderDate)

SQL Server stores data conceptually ordered like:

- CustomerID
   → OrderDate

So queries filtering by:

WHERE CustomerID = 'ALFKI'

or:

WHERE CustomerID = 'ALFKI'
AND OrderDate >= '1997-01-01'

can efficiently use the index.

But query:

WHERE OrderDate >= '1997-01-01'

may not efficiently use that same composite index because:

index starts with CustomerID,
SQL Server cannot efficiently jump directly by OrderDate alone.

## Important indexing principle

For composite indexes:

- left-most column matters first

Why this matters in analytics/business systems

## Good index/query alignment:

- improves dashboards,
- speeds up reports,
- reduces server load,
- improves scalability.

Poor alignment:

causes scans,
slower queries,
higher memory and CPU usage.

# Main benefits of indexing:
 - Faster (speed);
 - Higher capacity;
 - Costings;
 - Environmental benefits




