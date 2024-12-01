# Populate-Database

**1.	Data Generation**

•	Approach:

The dataset for this project was generated programmatically using Python and the Faker library. The Faker library allows for the creation of realistic, synthetic data, ensuring scalability and diversity while avoiding privacy concerns. A total of 000 records were generated for each table in the database.

•	Process:

o	Users: Generated random names, ages, genders, locations, and membership levels.
o	Products: Randomized product names, categories, prices, stock quantities, brands, and ratings.
o	Orders: Linked to users, with randomized order dates, total amounts, and payment methods.
o	OrderDetails: Linked to orders and products, detailing quantities, discounts, and feedback.

•	Tools Used:

o	Faker library: For generating realistic data.
o	SQLite: As the database system for storing and managing data.
o	Python (sqlite3 module): For database interactions.

**2.	Steps to Reproduce data**

•	Set Up Environment: Install Python and required libraries such as Faker and sqlite3.
•	Run the Python Script: Execute the data generation script to populate the database with 1000 rows in each table.
•	Query the Database: Use SQLite tools to interact with and analyze the database.

**4.	Justification**

•	Table Design:

o	Users: Designed to capture demographic and account-related information about customers.
o	 Products: Represents items available for sale, with attributes for pricing, stock, and customer reviews.
o	 Orders: Tracks purchases, linking customers to transactions.
o	 OrderDetails: Provides itemized details for each order.

•	Keys and Constraints:

o	Primary Keys: Ensure each record is uniquely identifiable (e.g., UserID, ProductID).
o	Foreign Keys: Enforce referential integrity between dependent tables.
o	NOT NULL Constraints: Ensure critical fields like Name and Product Name are Always populated.


