CREATE database Online_Store
USE Online_store;
CREATE TABLE Users (
    UserID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Age INTEGER,
    Gender TEXT,
    RegistrationDate DATE,
    Location TEXT,
    MemberLevel TEXT
);

CREATE TABLE Products (
    ProductID INTEGER PRIMARY KEY ,
    ProductName TEXT NOT NULL,
    Category TEXT,
    Price REAL,
    Stock INTEGER,
    Brand TEXT,
    Rating REAL
);

CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY ,
    UserID INTEGER,
    OrderDate DATE,
    TotalAmount REAL,
    Status TEXT,
    PaymentMode TEXT,
    ShippingCost REAL,
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

CREATE TABLE OrderDetails (
    OrderDetailID INTEGER PRIMARY KEY ,
    OrderID INTEGER,
    ProductID INTEGER,
    Quantity INTEGER,
    Discount REAL,
    Subtotal REAL,
    Feedback TEXT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);
