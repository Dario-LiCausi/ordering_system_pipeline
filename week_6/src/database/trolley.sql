DROP TABLE IF EXISTS trolleys CASCADE;

CREATE TABLE IF NOT EXISTS trolleys (
    trolley_id INTEGER GENERATED ALWAYS AS IDENTITY,
    order_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    PRIMARY KEY (trolley_id),
    FOREIGN KEY (item_id) REFERENCES items(item_id) ON DELETE CASCADE
    -- FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE
);

INSERT INTO trolleys (order_id, item_id)
VALUES 
    (1,15),
    (1,3),
    (1,19),
    (1,12),
    (2,2),
    (2,4),
    (2,22);


SELECT * FROM trolleys ORDER BY trolley_id ASC;