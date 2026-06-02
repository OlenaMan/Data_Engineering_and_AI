# Referencing with PyMongo – Star Wars Starships Project

## Whole Process

### 1. MongoDB Server Was Running

This means the database was available locally:

```text
mongodb://localhost:27017
```

MongoDB was already storing the `starwars` database and the `characters` collection that had been imported earlier.

---

### 2. Python Opened a Connection to MongoDB

```python
client = MongoClient(MONGO_URI)
db = client["starwars"]
```

This means:

* Python connects to MongoDB.
* PyMongo acts as the communication layer between Python and MongoDB.
* Python selects the `starwars` database.

---

### 3. Python Pulled Starships from the API

```python
starships = get_starships()
```

This sent a web request to:

```text
https://swapi.info/api/starships
```

and received 36 starship records.

---

### 4. Each Starship Had Pilot URLs

Example before transformation:

```python
"pilots": [
    "https://swapi.info/api/people/13",
    "https://swapi.info/api/people/14"
]
```

These are simply web links and are not MongoDB references.

---

### 5. Python Opened Each Pilot URL

For each pilot URL, Python requested the pilot data from the API and extracted the pilot's name.

Example:

```python
pilot_name = "Han Solo"
```

---

### 6. Python Searched MongoDB for That Character

```python
character = db.characters.find_one(
    {"name": pilot_name}
)
```

Python asked MongoDB:

> Find the character document where the name is "Han Solo".

MongoDB returned the matching document, including its `_id`.

Example:

```python
{
    "_id": ObjectId("6a1e90fd2ea13e89ae8e553c"),
    "name": "Han Solo"
}
```

---

### 7. Python Replaced the Pilot URL with the MongoDB ObjectId

Before:

```python
"pilots": [
    "https://swapi.info/api/people/14"
]
```

After:

```python
"pilots": [
    ObjectId("6a1e90fd2ea13e89ae8e553c")
]
```

This is the referencing step.

---

### 8. Python Inserted the Transformed Starships into MongoDB

```python
db.starships.insert_many(
    transformed_starships
)
```

MongoDB now contains a new collection:

```text
starships
```

containing 36 starship documents.

---

# What Referencing Means

Referencing means:

> One collection stores the `_id` values of documents that exist in another collection.

In this project:

```text
starships collection
```

references

```text
characters collection
```

through the `pilots` field.

---

### Example

```python
{
    "name": "Millennium Falcon",
    "pilots": [
        ObjectId("6a1e90fd2ea13e89ae8e553c"),
        ObjectId("6a1e90fded56f0634517b87f")
    ]
}
```

Those ObjectIds point to actual character documents:

```python
{
    "_id": ObjectId("6a1e90fd2ea13e89ae8e553c"),
    "name": "Han Solo"
}
```

---

# Why Not Store Full Pilot Data Inside Each Starship?

Because that would duplicate data.

Instead of storing:

```python
{
    "name": "Han Solo",
    "height": "180",
    "mass": 80,
    "homeworld": {...}
}
```

inside every starship document, we store only:

```python
ObjectId("6a1e90fd2ea13e89ae8e553c")
```

This reduces duplication and keeps the database consistent.

If Han Solo's data changes, it only needs to be updated once in the `characters` collection.

---

# Simple Mental Model

### Terminal

```text
Run the Python file.
```

Example:

```bash
python3 starships_reference.py
```

---

### Python

```text
Fetch API data.
Transform the data.
Connect to MongoDB.
Insert transformed documents.
```

---

### PyMongo

```text
Allows Python to communicate with MongoDB.
```

Examples:

```python
db.characters.find_one(...)
db.starships.insert_many(...)
```

---

### MongoDB

```text
Stores the transformed starship documents.
Stores the character documents.
Stores the references between them.
```

---

### Referencing

```text
Starship documents store character ObjectIds
instead of pilot URLs or duplicated pilot data.
```

Relationship:

```text
Starship
    ↓
Pilot ObjectId
    ↓
Character Document
```

This is MongoDB's equivalent of a foreign key relationship in relational databases.
