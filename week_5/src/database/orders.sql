DROP TABLE IF EXISTS orders CASCADE;
DROP TABLE IF EXISTS order_status CASCADE;

CREATE TABLE order_status (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    order_status VARCHAR(50) NOT NULL
);

INSERT INTO order_status (order_status) VALUES
('Preparing'),
('Delivered'),
('Cancelled'),
('Pending');

CREATE TABLE orders (
    order_id INTEGER GENERATED ALWAYS AS IDENTITY,
    customer_id INTEGER NOT NULL,
    courier_id INTEGER NOT NULL,
    status INTEGER NOT NULL,
    trolley_id INTEGER NOT NULL,
    PRIMARY KEY (order_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (courier_id) REFERENCES couriers(courier_id) ON DELETE CASCADE,
    FOREIGN KEY (status) REFERENCES order_status(id) ON DELETE CASCADE,
    FOREIGN KEY (trolley_id) REFERENCES trolleys(trolley_id) ON DELETE CASCADE
);

INSERT INTO orders (customer_id, courier_id, status, trolley_id)
VALUES (1, 1, 4, 1),
       (2, 3, 4, 1);