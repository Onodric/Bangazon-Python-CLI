DELETE FROM Customer;
DELETE FROM PaymentMethod;
DELETE FROM Product;
DELETE FROM Order;
DELETE FROM LineItems;

DROP TABLE IF EXISTS Customer;
DROP TABLE IF EXISTS PaymentMethod;
DROP TABLE IF EXISTS Product;
DROP TABLE IF EXISTS Order;
DROP TABLE IF EXISTS LineItems;



CREATE TABLE `Customer` (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	address TEXT NOT NULL,
	city TEXT NOT NULL,
	state TEXT NOT NULL,
	zip INTEGER NOT NULL,
	phone TEXT NOT NULL,
	active INTEGER NOT NULL
);

INSERT INTO Customer VALUES (null, 'Bob Ross', '1111 Awesome Lane', 'New York', "New York", 54321, "(111) 111-1111", 0)
INSERT INTO Customer VALUES (null, 'Donald Drumpf', '2222 Tiny Hands Drive', 'New York', "New York", 54321, "(222) 2222-2222", 0)
INSERT INTO Customer VALUES (null, 'Bugs Bunny', '3333 Carrot Boulevard', 'Albuquerque', "New Mexico", 54321, "(333) 333-3333", 0)



CREATE TABLE `PaymentMethod` (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    payment_type TEXT NOT NULL,
    description TEXT NOT NULL
    customer_id INTEGER NOT NULL,
);

INSERT INTO Product VALUES (null, 'coconut oil shampoo', 7.99, 'silky smoothe hair treatment shampoo');
INSERT INTO Product VALUES (null, 'Rusty Slinky', 20.00, 'The most fun toy that ever gave you Tetanus!');
INSERT INTO Product VALUES (null, 'Electric Guitar', 3.50, 'Fun way to make music.');



CREATE TABLE `Product` (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price NUMBER NOT NULL,
    description TEXT NOT NULL
);

INSERT INTO Product VALUES (null, 'coconut oil shampoo', 7.99, 'silky smoothe hair treatment shampoo');
INSERT INTO Product VALUES (null, 'Rusty Slinky', 20.00, 'The most fun toy that ever gave you Tetanus!');
INSERT INTO Product VALUES (null, 'Electric Guitar', 3.50, 'Fun way to make music.');



CREATE TABLE `Order`
                (
                    order_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    is_closed INTEGER NOT NULL,
                    payment_id INTEGER NOT NULL,
                    customer_id INTEGER NOT NULL,
                    FOREIGN KEY(`payment_id`) REFERENCES `Payment`(`payment_id`)
                    FOREIGN KEY(`customer_id`) REFERENCES `Customer`(`customer_id`)
                )



CREATE TABLE `LineItems`
                (
                    lineitem_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    order_id INTEGER NOT NULL,
                    product_id INTEGER NOT NULL,
                    FOREIGN KEY(`order_id`) REFERENCES `Order`(`order_id`)
                    FOREIGN KEY(`product_id`) REFERENCES `Product`(`product_id`)
                )


