import sqlite3
from faker import Faker
from random import randint, uniform, choice

# Initialize Faker
fake = Faker()

# Connect to the SQLite database
conn = sqlite3.connect('online_shop.db')
cursor = conn.cursor()

# Create Users table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        UserID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT,
        Age INTEGER,
        Gender TEXT,
        RegistrationDate TEXT,
        Location TEXT,
        MemberLevel TEXT
    )
""")

# Create Products table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products (
        ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
        ProductName TEXT,
        Category TEXT,
        Price REAL,
        Stock INTEGER,
        Brand TEXT,
        Rating REAL
    )
""")

# Create Orders table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Orders (
        OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
        UserID INTEGER,
        OrderDate TEXT,
        TotalAmount REAL,
        Status TEXT,
        PaymentMode TEXT,
        ShippingCost REAL,
        FOREIGN KEY (UserID) REFERENCES Users(UserID)
    )
""")

# Create OrderDetails table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS OrderDetails (
        OrderDetailID INTEGER PRIMARY KEY AUTOINCREMENT,
        OrderID INTEGER,
        ProductID INTEGER,
        Quantity INTEGER,
        Discount REAL,
        Subtotal REAL,
        Feedback TEXT,
        FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
        FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
    )
""")

# Generate 1000 rows for Users table
# ... (rest of the code remains the same)
# Generate 1000 rows for Products table
# Generate 1000 rows for Users table
def populate_users():
    users_data = []
    for _ in range(1000):
        name = fake.name()
        age = randint(18, 65)
        gender = choice(['Male', 'Female', 'Other'])
        registration_date = fake.date_between(start_date='-3y', end_date='today')
        location = fake.city()
        member_level = choice(['Bronze', 'Silver', 'Gold', 'Platinum'])
        users_data.append((name, age, gender, registration_date, location, member_level))
    cursor.executemany("""
        INSERT INTO Users (Name, Age, Gender, RegistrationDate, Location, MemberLevel)
        VALUES (?, ?, ?, ?, ?, ?)
    """, users_data)
    
def populate_products():
    products_data = []
    categories = ['Electronics', 'Clothing', 'Books', 'Home Appliances', 'Toys']
    brands = ['BrandA', 'BrandB', 'BrandC', 'BrandD']
    for _ in range(1000):
        product_name = fake.word().capitalize() + " " + choice(["Gadget", "Item", "Tool"])
        category = choice(categories)
        price = round(uniform(10, 2000), 2)
        stock = randint(0, 500)
        brand = choice(brands)
        rating = round(uniform(1, 5), 1)  # Ratings between 1.0 to 5.0
        products_data.append((product_name, category, price, stock, brand, rating))
    cursor.executemany("""
        INSERT INTO Products (ProductName, Category, Price, Stock, Brand, Rating)
        VALUES (?, ?, ?, ?, ?, ?)
    """, products_data)

# Generate 1000 rows for Orders table
def populate_orders():
    orders_data = []
    for _ in range(1000):
        user_id = randint(1, 1000)  # User IDs from the Users table
        order_date = fake.date_between(start_date='-1y', end_date='today')
        total_amount = round(uniform(50, 1000), 2)
        status = choice(['Pending', 'Shipped', 'Delivered', 'Cancelled'])
        payment_mode = choice(['Credit Card', 'PayPal', 'Bank Transfer', 'Cash on Delivery'])
        shipping_cost = round(uniform(5, 50), 2)
        orders_data.append((user_id, order_date, total_amount, status, payment_mode, shipping_cost))
    cursor.executemany("""
        INSERT INTO Orders (UserID, OrderDate, TotalAmount, Status, PaymentMode, ShippingCost)
        VALUES (?, ?, ?, ?, ?, ?)
    """, orders_data)

# Generate 1000 rows for OrderDetails table
def populate_order_details():
    order_details_data = []
    for _ in range(1000):
        order_id = randint(1, 1000)  # Order IDs from the Orders table
        product_id = randint(1, 1000)  # Product IDs from the Products table
        quantity = randint(1, 10)
        discount = round(uniform(0, 50), 2)
        subtotal = round(quantity * uniform(10, 200), 2)
        feedback = choice([None, fake.sentence()])
        order_details_data.append((order_id, product_id, quantity, discount, subtotal, feedback))
    cursor.executemany("""
        INSERT INTO OrderDetails (OrderID, ProductID, Quantity, Discount, Subtotal, Feedback)
        VALUES (?, ?, ?, ?, ?, ?)
    """, order_details_data)

# Populate all tables
populate_users()
populate_products()
populate_orders()
populate_order_details()

# Commit and close
conn.commit()
conn.close()

print("1000 rows inserted into each table!")
