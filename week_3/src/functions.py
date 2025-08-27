# import

import os
import json
import csv

# products

def load_products():
    file_path = os.path.join(os.path.dirname(__file__), '../data/products_list.json')
    with open(file_path, 'r') as file:
        return json.load(file)

def save_products(products):
    with open('products_list.json', 'w') as file:
        json.dump(products, file, indent=4)

products = load_products ()

# orders

def load_orders():
    file_path = os.path.join(os.path.dirname(__file__), '../data/orders.csv')
    orders = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            orders.append(row)
    return orders

def save_orders(orders):
    file_path = os.path.join(os.path.dirname(__file__), '../data/orders.csv')
    fieldnames = ["order_id", "customer_name", "cutomer_address", "customer_phone", "courier", "status"]
    with open(file_path, mode='w') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for order in orders:
            writer.writerow(order)

orders = load_orders ()

# courier
def load_couriers():
    file_path = os.path.join(os.path.dirname(__file__), '../data/couriers.json')
    with open(file_path, 'r') as file:
        return json.load(file)
    
def save_couriers(couriers):
    file_path = os.path.join(os.path.dirname(__file__), '../data/couriers.json')
    with open(file_path, 'w') as file:
        json.dump(couriers, file, indent=4)

couriers = load_couriers()

# menus

def main_menu():
    print("\nMain Menu\n")
    print("0. Exit")
    print("1. Items Menu")
    print("2. Couriers Menu")
    print("3. Orders menu")

def item_menu():
    print("\nItems Item\n")
    print("0. Back")
    print("1. Check Products")
    print("2. Create New Product")
    print("3. Update Product")
    print("4. Remove Product")

def order_menu():
    print("\nOrders Menu\n")
    print("0. Back")
    print("1. Check Orders")
    print("2. Place Order")
    print("3. Order Status")
    print("4. Update Existing Order")
    print("5. Delete Order")

def courier_menu():
    print("\nCourier Menu\n")
    print("0. Back")
    print("1. Print Courier List")
    print("2. Create new Courier")
    print("3. Update Courier")
    print("4. Delete Courier")

def category():
    print("\nProducts Category\n")
    print("0. Back")
    print("1. Pastry")
    print("2. Sandwich")
    print("3. Coffee")
    print("4. Tea")

# Item funcions

# add item

def add_product(prod_category):
    for index, item in enumerate(products[prod_category], start=1):
        print(f"{index}. {item}")

    new_product = input("\nAdd product: ").title()
    
    if new_product in products[prod_category]:
        print(f"\n{new_product} already in {prod_category}!\n")
        
    else:
        products[prod_category].append(new_product)
        print(f"\n{new_product} added to {prod_category}\n")
        save_products(products)
        category()

# update item

def update_product(prod_category):
    for index, item in enumerate(products[prod_category], start=1):
        print(f"{index}. {item}")
    
    update_product_name = int(input("\nChoose the product to update: "))-1

    if 0 <= update_product_name < len(products[prod_category]):
        old_name = products[prod_category][update_product_name]
        new_update = input("Enter the new product name: ").title()
        products[prod_category][update_product_name] = new_update
        print(f"\n{old_name} has been updated to {new_update}!\n")
        save_products(products)
        
        item_menu()

    else:
        print("\nTry again!\n")

# delete item

def del_product(prod_category):
    for index, item in enumerate(products[prod_category], start=1):
        print(f"{index}. {item}")
    
    elim_product = int(input('\nChoose the product to delete: '))-1

    if 0 <= elim_product < len(products[prod_category]):
        deleted_item = products[prod_category][elim_product]
        del products[prod_category][elim_product]
        print(f"\n{deleted_item} has been deleted.\n")
        item_menu()
    else:
        print("\nTry again: \n")

# Orders functions

# New order
def pick_courier():
    print_courier_list()
    courier_choice = int(input("\nSelect a courier: "))
    if 0 <= courier_choice < len(couriers["couriers"]):
         return couriers["couriers"][int(courier_choice) - 1]
    else:
        print("\nPlease try again.\n")
        return pick_courier()


def cust_info():
    print()
    order_id = f"order #{len(orders)+1}"
    cust_name = input("Name: ").title()
    cust_phone = input("Phone Number: ")
    cust_addr = input("Address: ").title()
    courier_numb = pick_courier()
    status = "Pending"

    new_order = {
        "order_id": order_id,
        "customer_name": cust_name,
        "cutomer_address": cust_addr,
        "customer_phone": cust_phone,
        "courier": courier_numb,
        "status": status
    }
    orders.append(new_order)
    print(f"\nOrder {order_id} added to queue!\n")
    save_orders(orders)

# print order list with details

def print_orders():
    print("\nOrders:\n")
    if not orders:
        print("There are no orders!\n")
        return

    for index, order in enumerate(orders, start=1):
        print(f"\nOrder {index}:")
        for key, value in order.items():
            print(f"  {key.replace('_', ' ').title()}: {value}")

# print order list

def print_order_list():
    print("\nOrders:\n")
    if not orders:
        print("There are no orders!\n")
        

    for index, order in enumerate(orders, start=1):
        print(f"{index}. Order ID: {order['order_id']}")
    return True

# select ord

def select_order():
    if not print_order_list():
        return None 

    select_ord = int(input("\nSelect order: ")) - 1

    if 0 <= select_ord < len(orders):
        return orders[select_ord] 
    else:
        print("\n! Try again: ")
        return None
    
# update status
def update_status():
    print("\nUpdate Order Status\n")
    selected_order = select_order()
    if selected_order:
        print("\nChange Order Status\n")
        status_options = ["PENDING", "PREPARING", "SHIPPED", "DELIVERED"]
        for i, status in enumerate(status_options, start=1):
            print(f"{i}. {status}")
        
        new_status_index = int(input("\nSelect status: ")) - 1
        
        if 0 <= new_status_index < len(status_options):
            new_status = status_options[new_status_index]
            selected_order["status"] = new_status
            
            print("\nStatus Updated!\n")
            save_orders(orders)
            print_order_list()
        else:
            print("\nTry again: ")

# update order
def update_order_details():
    print("\nUpdate Order\n")
    selected_order = select_order()
    if selected_order:
        print("\nUpdating Order Details\n")
        for key, value in selected_order.items():
            new_value = input(f"New value {key.replace('_', ' ').title()} (Leave blank to keep '{value}'): ").title()
            if new_value:
                selected_order[key] = new_value
        print("\nOrder Updated\n")
        save_orders(orders)
        print_order_list()

# delete order
def delete_order():
    print("\nDelete Order\n")
    selected_order = select_order()
    if selected_order:
        orders.remove(selected_order)
        print(f"\nOrder {selected_order['order_id']} has been deleted.\n")
        save_orders(orders)

# print couriers list

def print_courier_list():
    print("\nCouriers:\n")
    if len(couriers) == 0:
        print("No courier available!\n")
        return False
    for index, courier in enumerate(couriers["couriers"], start=1):
        print(f"{index}. {courier}")
    return True

# new courier

def new_courier():
    for index, item in enumerate(couriers["couriers"], start=1):
        print(f"{index}. {item}")

    new_name = input("\nAdd Courier's Name: ").title()
    
    if new_name in couriers["couriers"]:
        print(f"\n{new_name} already in the couriers list!\n")
        
    else:
        couriers["couriers"].append(new_name)
        print(f"\n{new_name} added to the couriers list\n")
        save_couriers(couriers)
    
# update courier
   
def update_courier():
    for index, item in enumerate(couriers["couriers"], start=1):
        print(f"{index}. {item}")
    
    update_courier_name = int(input("\nChoose the courier to update: "))-1

    if 0 <= update_courier_name < len(couriers["couriers"]):
        old_name = couriers["couriers"][update_courier_name]
        new_update = input("Enter the new product name: ").title()
        couriers["couriers"][update_courier_name] = new_update
        print(f"\n{old_name} has been updated to {new_update}!\n")
        save_couriers(couriers)
    else:
        print("\nTry again!\n")

def delete_courier():
    for index, item in enumerate(couriers["couriers"], start=1):
        print(f"{index}. {item}")
    
    elim_courier = int(input('\nChoose the product to delete: '))-1

    if 0 <= elim_courier < len(couriers["couriers"]):
        deleted_name = couriers["couriers"][elim_courier]
        del couriers["couriers"][elim_courier]
        print(f"\n{deleted_name} has been deleted.\n")
    else:
        print("\nTry again: \n")