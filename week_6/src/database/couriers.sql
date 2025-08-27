DROP TABLE IF EXISTS couriers CASCADE;

CREATE TABLE IF NOT EXISTS couriers (
    courier_id INTEGER GENERATED ALWAYS AS IDENTITY,
    courier_name VARCHAR(255) UNIQUE NOT NULL,
    courier_phone_number VARCHAR(20) UNIQUE NOT NULL,
    -- order_id INTEGER,
    PRIMARY KEY (courier_id)
    -- FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE SET NULL
);

INSERT INTO couriers (courier_name, courier_phone_number)
VALUES 
    ('Liselotte', '07533012345'),
    ('Sebastian', '07894321573'),
    ('Ayman', '07412345768'),
    ('Jane', '07463928457'),
    ('Hunter', '0743384757'),
    ('Markus', '0746373821'),
    ('Walter', '07433225967'),
    ('Zeze', '0754867532');