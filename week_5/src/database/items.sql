DROP TABLE IF EXISTS items CASCADE;

CREATE TABLE IF NOT EXISTS items (
    item_id INTEGER GENERATED ALWAYS AS IDENTITY,
    category VARCHAR(50) NOT NULL,
    item VARCHAR(100) UNIQUE NOT NULL,
    price DECIMAL(5,2) NOT NULL,
    PRIMARY KEY (item_id)
);

INSERT INTO items (category, item, price) VALUES 
    ('Pastry', 'Croissant', 2.50),
    ('Pastry', 'Pan au Chocolat', 2.80),
    ('Pastry', 'Brownie', 3.50),
    ('Pastry', 'Carrot Cake', 3.80),
    ('Pastry', 'Pastel de Nata', 2.70),
    ('Pastry', 'Almond Croissant', 3.20),
    ('Pastry', 'Chocolate Cake', 3.10),
    ('Sandwich', 'Coronation Chicken', 4.80),
    ('Sandwich', 'Ham And Cheese', 4.70),
    ('Sandwich', 'BLT', 5.00),
    ('Sandwich', 'Egg Mayo And Cress', 4.00),
    ('Salad', 'Caesar Salad', 5.10),
    ('Salad', 'Middle Eastern Tabbouleh', 5.40),
    ('Coffee', 'Americano', 3.00),
    ('Coffee', 'Flat White', 3.50),
    ('Coffee', 'Espresso', 2.20),
    ('Coffee', 'Cappuccino', 3.80),
    ('Coffee', 'Mocha', 4.00),
    ('Coffee', 'Latte', 3.60),
    ('Coffee', 'Cortado', 3.20),
    ('Tea', 'Earl Grey', 2.60),
    ('Tea', 'English Breakfast', 2.50),
    ('Tea', 'Green Tea', 2.80),
    ('Tea', 'Chai Latte', 3.50),
    ('Hot Pot', 'Beef And Barley', 6.10);