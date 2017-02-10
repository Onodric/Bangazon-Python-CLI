DELETE FROM LineItem;
DELETE FROM Orders;
DELETE FROM Product;
DELETE FROM Payment;
DELETE FROM Customer;

DROP TABLE IF EXISTS LineItem;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Product;
DROP TABLE IF EXISTS Payment;
DROP TABLE IF EXISTS Customer;



CREATE TABLE `Customer` (
	customer_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	address TEXT NOT NULL,
	city TEXT NOT NULL,
	state TEXT NOT NULL,
	postal INTEGER NOT NULL,
	phone TEXT NOT NULL,
	active INTEGER NOT NULL
);

INSERT INTO Customer VALUES (null, 'Bob Ross', '1111 Awesome Lane', 'New York', "New York", 54321, "(111) 111-1111", 0);
INSERT INTO Customer VALUES (null, 'Donald Trump', '2222 Tiny Hands Drive', 'New York', "New York", 54321, "(222) 2222-2222", 0);
INSERT INTO Customer VALUES (null, 'Bugs Bunny', '3333 Carrot Boulevard', 'Albuquerque', "New Mexico", 54321, "(333) 333-3333", 0);



CREATE TABLE `Payment` (
    payment_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    account_number TEXT NOT NULL,
    payment_type TEXT NOT NULL,
    customer_id INTEGER NOT NULL,
    FOREIGN KEY(`customer_id`) REFERENCES `Customer`(`customer_id`)
);

INSERT INTO Payment
	SELECT null, "1234567890", "VISA", c.customer_id
	FROM Customer c
	WHERE c.name = 'Bob Ross';

INSERT INTO Payment
	SELECT null, "0987654321", "Wells Fargo", c.customer_id
	FROM Customer c
	WHERE c.name = 'Donald Trump';

INSERT INTO Payment
	SELECT null, "000000000", "Bunny Bank", c.customer_id
	FROM Customer c
	WHERE c.name = 'Bugs Bunny';



CREATE TABLE `Product` (
    product_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price NUMBER NOT NULL,
    description TEXT NOT NULL
);

INSERT INTO Product VALUES (null, 'coconut oil shampoo', 7.99, 'silky smoothe hair treatment shampoo');
INSERT INTO Product VALUES (null, 'Rusty Slinky', 20.00, 'The most fun toy that ever gave you Tetanus!');
INSERT INTO Product VALUES (null, 'Electric Guitar', 3.50, 'Fun way to make music.');



CREATE TABLE `Orders` (
    orders_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    is_closed INTEGER NOT NULL,
    payment_id INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    FOREIGN KEY(`payment_id`) REFERENCES `Payment`(`payment_id`),
    FOREIGN KEY(`customer_id`) REFERENCES `Customer`(`customer_id`)
);

INSERT INTO Orders
	SELECT null, 0, p.payment_id, c.customer_id
	FROM Payment p, Customer c
	WHERE p.payment_type = "VISA" AND c.name = "Bob Ross";

INSERT INTO Orders
	SELECT null, 0, p.payment_id, c.customer_id
	FROM Payment p, Customer c
	WHERE p.payment_type = "Wells Fargo" AND c.name = "Donald Trump";

INSERT INTO Orders
	SELECT null, 1, p.payment_id, c.customer_id
	FROM Payment p, Customer c
	WHERE p.payment_type = "Bunny Bank" AND c.name = "Bugs Bunny";



CREATE TABLE `LineItem`(
    line_item_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    orders_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    FOREIGN KEY(`orders_id`) REFERENCES `Orders`(`orders_id`),
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`product_id`)
);

INSERT INTO LineItem
	SELECT null, o.orders_id, p.product_id
	FROM Product p, Orders o, Customer c
	WHERE p.name = "coconut oil shampoo" AND c.name="Bob Ross" AND o.customer_id = c.customer_id;

INSERT INTO LineItem
	SELECT null, o.orders_id, p.product_id
	FROM Product p, Orders o, Customer c
	WHERE p.name = "Rusty Slinky" AND c.name="Donald Trump" AND o.customer_id = c.customer_id;

INSERT INTO LineItem
	SELECT null, o.orders_id, p.product_id
	FROM Product p, Orders o, Customer c
	WHERE p.name = "Electric Guitar" AND c.name="Bugs Bunny" AND o.customer_id = c.customer_id;




