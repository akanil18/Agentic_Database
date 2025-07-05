import sqlite3

# Step 1: Connect to SQLite DB
conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()

# Step 2: Drop all user-defined tables (ignore internal SQLite tables)
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
tables = cursor.fetchall()
for table in tables:
    table_name = table[0]
    print(f"🗑 Dropping table: {table_name}")
    cursor.execute(f"DROP TABLE IF EXISTS {table_name};")

# Step 3: Create Products table
cursor.execute("""
CREATE TABLE Products (
    product_id INTEGER PRIMARY KEY,
    low_fats TEXT CHECK(low_fats IN ('Y', 'N')),
    recyclable TEXT CHECK(recyclable IN ('Y', 'N'))
);
""")

products_data = [
    (0, 'Y', 'N'),
    (1, 'Y', 'Y'),
    (2, 'N', 'Y'),
    (3, 'Y', 'Y'),
    (4, 'N', 'N')
]

cursor.executemany("INSERT INTO Products (product_id, low_fats, recyclable) VALUES (?, ?, ?);", products_data)

# Step 4: Create Customer table
cursor.execute("""
CREATE TABLE Customer (
    id INTEGER PRIMARY KEY,
    name TEXT,
    referee_id INTEGER
);
""")

customer_data = [
    (1, 'Will', None),
    (2, 'Jane', None),
    (3, 'Alex', 2),
    (4, 'Bill', None),
    (5, 'Zack', 1),
    (6, 'Mark', 2)
]

cursor.executemany("INSERT INTO Customer (id, name, referee_id) VALUES (?, ?, ?);", customer_data)

# Step 5: Create World table
cursor.execute("""
CREATE TABLE World (
    name TEXT,
    continent TEXT,
    area INTEGER,
    population INTEGER,
    gdp BIGINT
);
""")

world_data = [
    ("Afghanistan", "Asia", 652230, 25500100, 20343000000),
    ("Albania", "Europe", 28748, 2831741, 12960000000),
    ("Algeria", "Africa", 2381741, 37100000, 188681000000),
    ("Andorra", "Europe", 468, 78115, 3712000000),
    ("Angola", "Africa", 1246700, 20609294, 100990000000)
]

cursor.executemany("INSERT INTO World (name, continent, area, population, gdp) VALUES (?, ?, ?, ?, ?);", world_data)

cursor.execute("""
CREATE TABLE Visits (
    visit_id INTEGER PRIMARY KEY,
    customer_id INTEGER
);
""")

# Insert data into Visits
visits_data = [
    (1, 23),
    (2, 9),
    (4, 30),
    (5, 54),
    (6, 96),
    (7, 54),
    (8, 54)
]
cursor.executemany("INSERT INTO Visits (visit_id, customer_id) VALUES (?, ?);", visits_data)

# Create Transactions table
cursor.execute("""
CREATE TABLE Transactions (
    transaction_id INTEGER PRIMARY KEY,
    visit_id INTEGER,
    amount INTEGER
);
""")

# Insert data into Transactions
transactions_data = [
    (2, 5, 310),
    (3, 5, 300),
    (9, 5, 200),
    (12, 1, 910),
    (13, 2, 970)
]
cursor.executemany("INSERT INTO Transactions (transaction_id, visit_id, amount) VALUES (?, ?, ?);", transactions_data)

cursor.execute("""
CREATE TABLE Employee (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    managerId INTEGER
);
""")

# Insert data into Employee table
employee_data = [
    (101, 'John', 'A', None),
    (102, 'Dan', 'A', 101),
    (103, 'James', 'A', 101),
    (104, 'Amy', 'A', 101),
    (105, 'Anne', 'A', 101),
    (106, 'Ron', 'B', 101)
]

cursor.executemany("INSERT INTO Employee (id, name, department, managerId) VALUES (?, ?, ?, ?);", employee_data)


# Drop old tables
cursor.execute("DROP TABLE IF EXISTS Signups;")
cursor.execute("DROP TABLE IF EXISTS Confirmations;")

# Create Signups table
cursor.execute("""
CREATE TABLE Signups (
    user_id INTEGER PRIMARY KEY,
    time_stamp TEXT
);
""")

# Create Confirmations table
cursor.execute("""
CREATE TABLE Confirmations (
    user_id INTEGER,
    time_stamp TEXT,
    action TEXT CHECK(action IN ('confirmed', 'timeout')),
    PRIMARY KEY (user_id, time_stamp),
    FOREIGN KEY (user_id) REFERENCES Signups(user_id)
);
""")

# Insert data into Signups
signups_data = [
    (3, '2020-03-21 10:16:13'),
    (7, '2020-01-04 13:57:59'),
    (2, '2020-07-29 23:09:44'),
    (6, '2020-12-09 10:39:37'),
]
cursor.executemany("INSERT INTO Signups (user_id, time_stamp) VALUES (?, ?);", signups_data)

# Insert data into Confirmations
confirmations_data = [
    (3, '2021-01-06 03:30:46', 'timeout'),
    (3, '2021-07-14 14:00:00', 'timeout'),
    (7, '2021-06-12 11:57:29', 'confirmed'),
    (7, '2021-06-13 12:58:28', 'confirmed'),
    (7, '2021-06-14 13:59:27', 'confirmed'),
    (2, '2021-01-22 00:00:00', 'confirmed'),
    (2, '2021-02-28 23:59:59', 'timeout'),
]
cursor.executemany("INSERT INTO Confirmations (user_id, time_stamp, action) VALUES (?, ?, ?);", confirmations_data)
# Step 6: Commit and close
conn.commit()
conn.close()

print("🎉 All tables (Products, Customer, World) created and populated successfully.")
