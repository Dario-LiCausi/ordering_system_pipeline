DROP TABLE IF EXISTS customer_address CASCADE;

CREATE TABLE IF NOT EXISTS customer_address(
    address_id INTEGER GENERATED ALWAYS AS IDENTITY,
    house_numb INTEGER NOT NULL,
    street VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    post_code VARCHAR(20) NOT NULL,
    -- customer_id INTEGER NOT NULL,
    PRIMARY KEY (address_id)
    -- FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

INSERT INTO customer_address (house_numb, street, city, post_code)
VALUES
    (55, 'Valley Road', 'London', 'E24TJ'),
    (20, 'Oasis Avenue', 'London', 'NW13JE');