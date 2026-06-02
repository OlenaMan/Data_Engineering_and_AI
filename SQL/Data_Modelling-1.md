Intro to data modelling
# Intro to Data Modelling

## Data Modelling

When we need to store data we need to think about the different options and how we are going to plan out this storage.

Assuming we need a relational database, the main thing we need to think about is our tables and the relationships between them.

## The scenario

Our scenario will be:
- We run an online shop
- We have customers, orders and products
- Orders ccan contain multiple products

The question is: "How should we store this data in a table or tables?"

| OrderID | CustomerName | Product1 | Product2 | Product3 |

That makes sense, BUT it is not right. We need to fix a few things here.
- What is an order has 10 products?
- What if the customer name changes?
- How do we store multiple orders per customer?
- What if two products have the same name?

## Core data modelling concepts

Entities = essentially "things"

In our case thats:
- Customers
- Orders
- Products
- Etc.

Relationships = Links between Entities
- Customer to Orders (1-to-many)
- Orders to Products (many-to-many)

Keys = Anchor points for relationships between tables
- Primary Key = Unique Identifier (Usually an ID or Numeric value)
- Foreign Key = Column from another table, is the link/relationship between the two tables. Links two tables together.

## Building a model example

Step 1 - Customers Table
| CustomerID (PK) | Name | Email |

Step 2 - Orders
| OrderID (PK) | CustomerID (FK) | OrderDate |

Step 3 - Products
| ProductID (PK) | ProductName | Price |

Okay now comes the harder part, we have some questions to solve:
- Can one order have multiple products?
- Can one product appear in many orders?

The answer is yes, but we need properly set up Many-to-Many relationships.

## Bridge Tables

We need a bridge table that will have out many-to-many relationships. we will call it "OrderDetails".

| OrderID (FK) | ProductID (FK) | Quantity |

## Final Schema example

- Customers
- Orders
- OrderDetails
- Products

## SQL Example

If we made a blank DB with this schema, an example JOIN would be:
```SQL
SELECT *
FROM Orders o
JOIN OrderDetails od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID;
```

## Practical Normalisation

Rule 1 - No repeating columns

Bad:
```
Product1, Product2, Product3
```
Good:
```
Products
```

Rule 2 - Each table should contain a single "Entity" or "thing"

Rule 3 - No duplicated data
e.g CustomerName is not repeated on every order