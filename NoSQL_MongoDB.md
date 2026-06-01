# MongoDB & NoSQL

## 1. What are the different types of NoSQL databases?

NoSQL ("Not Only SQL") databases are designed to handle:

- Large volumes of data
- Flexible schemas
- High scalability

There are four main types of NoSQL databases:

### 1. Key-Value Databases

Store data as a key-value pair.

Example:

```json
{
  "user123": {
    "name": "John",
    "age": 30
  }
}
```

Examples:
- Redis
- Amazon DynamoDB

Use Cases:
- Caching
- Session management
- Shopping carts

---

### 2. Document Databases

Store data as documents, usually in JSON-like format.

Example:

```json
{
  "name": "John",
  "age": 30,
  "skills": ["Python", "SQL"]
}
```

Examples:
- MongoDB
- CouchDB

Use Cases:
- Web applications
- User profiles
- Content management systems

---

### 3. Column-Family Databases

Store data by columns rather than rows.

Examples:
- Apache Cassandra
- Apache HBase

Use Cases:
- Big data analytics
- IoT systems
- Real-time processing

---

### 4. Graph Databases

Store entities and their relationships.

Example:

```text
John --> FRIEND --> Sarah
```

Examples:
- Neo4j
- Amazon Neptune

Use Cases:
- Social networks
- Fraud detection
- Recommendation engines

---

# 2. What type of database is MongoDB?

MongoDB is a:

## Document-Oriented NoSQL Database

It stores information as documents rather than rows and tables.

### Traditional SQL

| CustomerID | Name | Age |
|------------|------|------|
| 1 | John | 30 |

### MongoDB

```json
{
  "_id": 1,
  "name": "John",
  "age": 30
}
```

Documents are stored inside **Collections**.

### SQL vs MongoDB

| SQL | MongoDB |
|------|----------|
| Database | Database |
| Table | Collection |
| Row | Document |
| Column | Field |

---

# 3. How does MongoDB work?

MongoDB stores data as BSON documents.

## BSON

**BSON = Binary JSON**

Example:

```json
{
  "_id": 1,
  "name": "John",
  "skills": ["Python", "SQL"],
  "address": {
    "city": "London"
  }
}
```

MongoDB converts JSON-like documents into BSON internally for efficient storage and retrieval.

---

## Structure

```text
MongoDB Server
└── Database
    └── Collection
        └── Documents
```

Example:

```text
CompanyDB
└── Employees
    ├── Employee 1
    ├── Employee 2
    └── Employee 3
```

---

## Query Example

### SQL

```sql
SELECT *
FROM Employees
WHERE age > 30;
```

### MongoDB

```javascript
db.employees.find(
  { age: { $gt: 30 } }
)
```

---

# 4. Why is MongoDB so popular?

## Flexible Schema

Documents can have different structures.

### Document 1

```json
{
  "name": "John",
  "age": 30
}
```

### Document 2

```json
{
  "name": "Sarah",
  "age": 28,
  "department": "IT"
}
```

No schema changes are required.

---

## Easy for Developers

Applications commonly use JSON.

MongoDB stores JSON-like documents, reducing data transformation.

---

## High Performance

Supports:

- Indexing
- Fast reads
- Fast writes
- In-memory processing

---

## Horizontal Scalability

Data can be distributed across multiple servers using **Sharding**.

---

## Cloud-Friendly

Commonly used in:

- Cloud-native applications
- APIs
- Microservices
- Modern web platforms

---

# 5. What use cases does MongoDB have?

## E-Commerce

Stores:

- Products
- Customer profiles
- Orders
- Shopping carts

Example:

```json
{
  "name": "Laptop",
  "ram": "16GB"
}
```

```json
{
  "name": "T-Shirt",
  "size": "M"
}
```

MongoDB easily handles different product structures.

---

## Content Management Systems

Stores:

- Articles
- Blogs
- Videos
- Metadata

---

## Mobile Applications

Stores:

- User profiles
- Messages
- Notifications
- Preferences

---

## Real-Time Analytics

Supports:

- Logging
- Monitoring
- Event tracking

---

## IoT Applications

Stores sensor data.

Example:

```json
{
  "device": "Sensor01",
  "temperature": 21.5,
  "timestamp": "2026-05-30"
}
```

---

## Social Media Platforms

Stores:

- Posts
- Comments
- Likes
- User profiles

---

# 6. What are Replica Sets?

A **Replica Set** is a group of MongoDB servers that maintain identical copies of data.

Purpose:

- High availability
- Disaster recovery
- Fault tolerance

Example:

```text
Primary Server
      ↓
Secondary Server
      ↓
Secondary Server
```

---

## Primary Node

Handles:

- Writes
- Updates
- Deletes

---

## Secondary Nodes

Continuously replicate data from the Primary.

If the Primary fails:

```text
Primary crashes
        ↓
Automatic election
        ↓
Secondary becomes Primary
```

Applications continue running with minimal interruption.

---

## Benefits

- Automatic failover
- High availability
- Backup capability
- Improved reliability

---

# 7. What is Sharding?

**Sharding = Horizontal Scaling**

Instead of storing all data on one server:

```text
Server 1
100 TB Data
```

Data is distributed across multiple servers:

```text
Shard 1 → 25 TB
Shard 2 → 25 TB
Shard 3 → 25 TB
Shard 4 → 25 TB
```

---

## How Sharding Works

MongoDB uses a **Shard Key**.

Example:

```text
customer_id
```

Data distribution:

```text
Customers 1–1000     → Shard 1
Customers 1001–2000  → Shard 2
Customers 2001–3000  → Shard 3
```

---

## Benefits

- Supports massive datasets
- Improves performance
- Handles millions of users
- Enables horizontal scaling

---

 MongoDB is a document-oriented NoSQL database that stores data as flexible BSON documents rather than rows and tables. Unlike relational databases, MongoDB does not require a fixed schema, making it ideal when data structures change frequently. It is popular because it is developer-friendly, scalable, and performs well with large volumes of data. Common use cases include e-commerce platforms, content management systems, mobile applications, real-time analytics, and IoT solutions. For high availability, MongoDB uses replica sets, where secondary nodes maintain copies of data and can automatically take over if the primary node fails. For horizontal scaling, MongoDB uses sharding, which distributes data across multiple servers to support large datasets and high traffic workloads.

# Vertical vs Horizontal Scaling

## Vertical Scaling (Scale Up)

Vertical scaling means making a **single server more powerful**.

### Example

| Before | After |
|----------|----------|
| 16 GB RAM | 64 GB RAM |
| 4 CPU cores | 16 CPU cores |
| 500 GB SSD | 2 TB SSD |

```text
Small Server
      ↓
Bigger Server
```

### Advantages

- Easy to implement
- No application changes required
- Simple architecture

### Disadvantages

- Expensive
- Physical hardware limits exist
- Single point of failure

### Example

A SQL Server database becomes slow.

Solution:

- Add RAM
- Add CPUs
- Upgrade storage

This is **Vertical Scaling**.

---

# Horizontal Scaling (Scale Out)

Horizontal scaling means adding **more servers** instead of making one server bigger.

### Example

```text
Server 1
Server 2
Server 3
Server 4
```

The workload is distributed across multiple servers.

### Advantages

- Almost unlimited growth
- Better fault tolerance
- High availability
- Reduced reliance on a single server

### Disadvantages

- More complex architecture
- Data distribution is required
- More difficult to manage

---

# MongoDB and Horizontal Scaling

MongoDB was designed with horizontal scaling in mind.

It achieves this using **Sharding**.

## Without Sharding

```text
Server 1
100 TB Data
```

## With Sharding

```text
Shard 1 → 25 TB
Shard 2 → 25 TB
Shard 3 → 25 TB
Shard 4 → 25 TB
```

Each server stores part of the total dataset.

This allows MongoDB to handle extremely large datasets and high traffic volumes.

---

# SQL Server vs MongoDB

## SQL Server

Traditionally scales vertically.

```text
More RAM
More CPU
Faster Storage
```

Although modern SQL Server supports some horizontal scaling options, vertical scaling remains the most common approach.

---

## MongoDB

Designed for horizontal scaling from the beginning.

```text
More Servers
More Shards
More Capacity
```

This makes MongoDB particularly suitable for large-scale distributed systems.

---

## Simple Analogy

Imagine a supermarket.

## Vertical Scaling

There is only one checkout.

Make it faster:

```text
1 Cashier
     ↓
Super-Fast Cashier
```

Still only one checkout exists.

---

## Horizontal Scaling

Add more checkouts:

```text
Checkout 1
Checkout 2
Checkout 3
Checkout 4
```

More customers can be served simultaneously.

---



Vertical scaling means increasing the power of a single server by adding CPU, RAM, or storage. Horizontal scaling means adding more servers and distributing the workload across them. MongoDB is designed for horizontal scaling through sharding, allowing data to be spread across multiple servers. This makes it easier to handle very large datasets and high traffic volumes compared with relying on a single increasingly powerful server.

# Intro to MongoDB tasks (notes from Class)

MongoDB is a document database that stores JASON-like documents, which allows you to store data with flwexible schema and provides quering and aggregation tools for access and analysis.

## MongoDB Use Cases and advantages/disadvantages

Advantages:
- Document Oriented Storage
- Easy scaling (horizontal)
- Fast/Efficient
- 'Open Source':
  - Publicly available;
  - Source code can be edited/chaged at will;
  - Free to use, at scale - no license fees etc.
  - Code can be distributed at will
  - Avoid vendor locking (when business becomes so deeply dependent on a specific cloud provider's services)
  - Flexible

Disadvantages:
- High memory usage and data redundancy;
- Can be inconsistent
- Unsupported transactions

Use Cases:
- Social Media posts/data
- Mobile Apps
- Caching (memory storage):
  - e.g.shopping carts
- Product info
- Media files/data
- CRM systems:
    - heavy text aspects
- IoT and Sensor data
- Logs and monitoring data
- Gaming data (log-ins, actions on server)
- Chat systems/apps
- etc.

E-commerse and Gaming are great industries to use NoSQL

### Connecting to MongoDB locally using Compass:
  - Start MongoDB service
  - Open MongoDB Compass
  - Click **New Connection**
  - Enter:
  ```
  mongodb://localhost:27017
  ```
  - Click **Connect**

Important:

- localhost = your own computer

- 27017 = MongoDB default port


### Writing scripts on Mongosh (MongoDB shell)

**use** command to create a new database
```
use sparta
```
**createCollection()** method to create collection
```
use sparta
db.createCollection("institute")
```

Insert data into collection:
```
db.institute.insertOne({name:"New document"})
```

Add multiple documents in one command
```
db.institute.insertMany([{"course": "Data Engineering"}, {"course": "Data Analysis"}])
```

## Validation
Use JASON Schema validation **$jsonSchema** when creating the collection to validate documents in the collection.

Example: create a new document **Students** where each document must have name, age, and course.
```
db.createCollection("Students", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["name", "age", "course"],
            properties: {
                name: {
                    bsonType: "string",
                    description: "Name must be a string and is required"
                },
                age: {
                    bsonType: "int",
                    minimum: 16,
                    description: "Age must be an integer and at least 16"
                },
                course: {
                    bsonType: "string",
                    enum: ["Data Engineering", "Data Analysis", "Data Science"],
                    description: "Course must be one of the approved values"
                }
            }
        }
    }
})
```
Valid document:
```
db.Students.insertOne({
    name: "Olena",
    age: 40,
    course: "Data Analysis"
})
```
When valid, MongoDB sends an acknowledgment
```
{
  acknowledged: true,
  insertedId: ObjectId("683c123456789abcdef12345")
}
```
Invalid document:
```
db.Students.insertOne({
    name: "Olena",
    age: "40",
    course: "Data Analysis"
})
```
This fails because age is a string.
MongoDB sends TypeError: Document failed validation
```
MongoServerError: Document failed validation
Details:
- age must be of type int
```
