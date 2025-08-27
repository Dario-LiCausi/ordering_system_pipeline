import csv
import os

from database.db_items import DbItems
from database.db_couriers import DbCouriers
from classes.main_class import Main_class

class Orders(Main_class):

    def __init__(self):
        super().__init__("/app/data/orders.csv", 
                         [
                          "order_id", 
                          "customer_name", 
                          "customer_address", 
                          "customer_phone", 
                          "courier_id", 
                          "status",
                          "items" 
                          ])
    
        self.products = DbItems()
        self.couriers = DbCouriers()

    def print_items(self, action="\nOrders List\n"):
        print(action.title())

        if not self.items:
            print("Orders list is empty!")
            return

        for index, item in enumerate(self.items, start=1):
            items_list = item.get("items", "").strip().split(",") if item.get("items") else []

            items_list = [item.strip() for item in items_list if item.strip().isdigit()]

            print(f"{index}. Order #{item['order_id']}\n")
            print(f"\tCustomer: {item['customer_name']}")
            print(f"\tAddress: {item['customer_address']}")
            print(f"\tPhone: {item['customer_phone']}")
            print(f"\tCourier ID: {item['courier_id']}")
            print(f"\tStatus: {item['status'].upper()}")
            print(f"\tItems: {', '.join(items_list) if items_list else 'No items selected'}\n")

    def select_products(self):
        print("\nSelect products:")
        self.products.print_item()
        
        selected = input("\nEnter product: ").split(",")
        
        try:
            shopping_list = [int(prod.strip()) for prod in selected if prod.strip().isdigit()]
            return shopping_list
        except ValueError:
            print("\nInvalid selection! Try again")
            return self.select_products()

    def add_item(self):
        print("\nCreate new order\n")

        selected_products = self.select_products()
        new_order_prod =  ",".join([str(item) for item in selected_products])

        new_order = {
            "order_id": str(len(self.items) + 1),
            "customer_name": input("Name: ").title(),
            "customer_address": input("Address: ").title(),
            "customer_phone": input("Phone number: "),
            "items": new_order_prod
        }

        print("\nAvailable Couriers:")
        self.couriers.print_couriers()

        new_order["courier_id"] = input("\nSelect Courier: ")
        new_order["status"] = "PREPARING"
        self.items.append(new_order)
        self.save_file()

        print(f"\nOrder #{new_order['order_id']} added for {new_order['customer_name']}!\n")