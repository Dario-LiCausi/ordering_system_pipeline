DROP TABLE IF EXISTS customer CASCADE;

CREATE TABLE IF NOT EXISTS customers(
    customer_id INTEGER GENERATED ALWAYS AS IDENTITY,
    customer_name VARCHAR(255) NOT NULL,
    customer_phone_number INTEGER NOT NULL,
    customer_address_id INTEGER NOT NULL,
    order_id INTEGER,
    PRIMARY KEY (customer_id),
    FOREIGN KEY (customer_address_id) REFERENCES customer_address(address_id) ON DELETE CASCADE
    -- FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE
);

INSERT INTO customers (customer_name, customer_phone_number, customer_address_id)
VALUES 
    ('Hammet Brown',0745680953,1),
    ('Wane Watson',0745673845,2);
