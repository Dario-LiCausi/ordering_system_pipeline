SELECT
    c.customer_id,
    c.customer_name,
    c.customer_phone_number,
    
    ca.house_numb,
    ca.street,
    ca.city,
    ca.post_code,
    
    o.order_id,
    o.status,
    cr.courier_name,
    cr.courier_phone_number,
    
    i.item AS item_name,
    i.price AS item_price
    
FROM customers AS c
JOIN customer_address AS ca ON ca.customer_id = c.customer_id
JOIN orders AS o ON c.order_id = o.order_id
JOIN couriers AS cr ON o.courier_id = cr.courier_id
JOIN trolleys AS t ON o.order_id = t.order_id
JOIN items AS i ON t.item_id = i.item_id
    
ORDER BY o.order_id, t.trolley_id;
