# import

import os
import csv

# parent class.
# OOP - main class to set the reles of all the main and repetetive functions/methods.
# load/read and write/save data in the respective csv files.
# if fielname is not found it is assigned to an empty list

class Main_class:
    
    def __init__(self, file_path="default.csv", fieldnames=None, **kwargs):
        if fieldnames is None:  
            fieldnames = []
        self.file_path = file_path
        self.fieldnames = fieldnames
        self.items = self.load_file()

# load_file if there is a file, it converts it (the csv file) in a dictionary and returns it
# if the file doesnt exists it returns in a empty list []

    def load_file(self):
        file_path = os.path.join(os.path.dirname(__file__), self.file_path)
        if not os.path.exists(file_path):  
            return []
        with open(file_path, "r", newline="") as file:
            reader = csv.DictReader(file)
            return list(reader)
    
    def save_file(self):
        file_path = os.path.join(os.path.dirname(__file__), self.file_path)
        with open(file_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(self.items)

    # print items list by iterating through the dictionary loaded from the CSV data file.   
    # <action> is a place holder argument that allows me to personalize the method to each different child class.
    # <if not> to check if the dictionary is empty or not.
    # <.strip()> is a method that removes white spaces.
    # <enumerate()> is a function useful to assign an index number to an iterable and returns it as an enumerate object.
    # <.get()> is a method that retrieves the value of a dictionary
    # index += 1 ensures the numbering starts from 1 instead of 0 
    # the for loop iterates every item in the dictionary to estract it and return it

    def print_items(self, action="\nItems Name\n"):
        print(action.title())
        if not self.items:
            print(f"{action.strip()} is empty!\n")
            return
        for index, item in enumerate(self.items, start=1):
            item_name = item.get("courier_name", "unknown item")
            print(f"{index}. {item_name.replace('_', ' ')}")

    def select_items(self, action = "\nSelect an Item: "):
        print(action.title())
        self.print_items()
        try:
            selected_index = int(input(f"\n{action}: ")) - 1
            if 0 <= selected_index < len(self.items):
                return self.items[selected_index]
            else:
                print("\nInvalid selection. Try again.")
                return None
        except ValueError:
            print("Invalid input! Please enter a number.")
            return None
        
    # append new item.
    # save to file.

    def add_item(self, new_item):
        self.items.append(new_item)
        self.save_file()
        print(f"\n{new_item} added to {list}")

# check if the selected index is in the dictionary range than updates it.

    def edit_item_index(self, index, updt_item, action):
        if 0 <= index < len(self.items):
            self.item[index].update(updt_item)
            self.save_file()
            print(f"{index} updated to {updt_item}")

# updates a selected item.
# if the selected index is not in range the function restarts.
# update the selected item. leave blank to not update that specific key.
# replaces underscores of var names with white space.
# if no new value is entered the key value doesnt update.


    def edit_item(self, action = "item"):
        selected_item = self.select_items(f"\nChoose the {action} to update: \n") 
        if selected_item is None:
            print("\nInvalid entry, try Again")
            return
        print(f"\nUpdating {action.title()} Details\n")
        for key, value in selected_item.items():
            updt = input(f"New value {key.replace('_', ' ').title()} (Leave blank to keep '{value}'): ").title()
            if updt:
                selected_item[key] = updt
        print(f"\n{action.title()} Updated\n")
        self.save_file()

# delete a selected item.
# calls back the select_items() method.
# it there the imput is a wrong key or not in index range the function restarts.
# save file function.

    def delete_item(self, action):
        selected_item = self.select_items(f"\nChoose the {action} to delete: ")
        if selected_item is None:
            print("\nInvalid entry, try Again")
            return
        self.items.remove(selected_item)
        print(f"\n{action.title()} has been removed")
        self.save_file()

# products class
# super.__init__ is a method that calls and override the parent class for loading the right csv file.

class Products(Main_class):
 
    def __init__(self):
        super().__init__("../data/products_list.csv", 
                         [
                             "category", 
                             "item", 
                             "price"
                             ]
                         )
# calls the parents parameters and override the action placeholder parameter values. 
#   
    def print_items(self, action="\nMenu\n"):
        print(action.title())

        if not self.items:
            print(f"{action.strip()} is empty!\n")
            return

# creates and empty dictionary that stores the items mapping between the actual index number and the printed index number (so it starts from 1).
# sorted() is a function that extracts the values of the category key and makes them unique.
# douple for loop, the first one iterats through the category keys and the second one iterates through the items.
# it's a way to format and organize the products dictionary when printed.
# return the index mapping value.

        index_mapping = {}
        index = 1

        categories = sorted({item["category"] for item in self.items})

        for category in categories:
            print(f"\n{category}:")

            for actual_index, item in enumerate(self.items):
                if item["category"] == category:
                    print(f"  {index}. {item['item']} - £{float(item['price']):.2f}")
                    index_mapping[index] = actual_index
                    index += 1

        return index_mapping

# calling back the select_item function and averride the action parameter.

    def select_items(self, action="Select a product:"):
    
        print(action.title())

        index_mapping = self.print_items("Product List")

# try / except checks if the input is a valid key.
# if checks if the input value is in the index range.

        try:
            selected_index = int(input("\nSelect a product: "))  
            if selected_index in index_mapping:
                real_index = index_mapping[selected_index]
                return self.items[real_index]
            else:
                print("\nInvalid selection. Try again.")
                return None
        except ValueError:
            print("\nInvalid input! Please enter a number.")
            return None

# overrides the products dictionary in the parent class function.

    def add_item(self):
        self.print_items("products")

        new_product = { 
            "item" : input("\nAdd product: ").title(),
            "category": input("Enter category: ").title(),
        }

# checks is the price value is a float
# if checks that the value is a positive number.
# .2f to only accept a 0.00 float value input.

        while True:
            price_input = input("Enter price (£0.00): ")
            try:
                price = float(price_input)
                if price < 0:
                    print("Price cannot be negative. Try again.")
                    continue
                new_product["price"] = f"{price:.2f}"
                break
            except ValueError:
                print("Invalid entry")

        self.items.append(new_product)
        self.save_file()
        print(f"\n{new_product['item']} - £{new_product['price']} added to {new_product['category']}!\n")

# couriers class
# super.__init__ is a method that calls and override the parent class for loading the right csv file.

class Couriers(Main_class):

    def __init__(self):
        super().__init__("../data/couriers.csv", 
                         [
                             "courier_id", 
                          "courier_name", 
                          "courier_phone_number"
                          ]
                         )
    def print_items(self):
        
        if not self.items:
            print(f"{self.items.strip()} is empty!\n")
            return
        for index, item in enumerate(self.items, start=1):
            print(f"{index}. {item['courier_name']} - {item['courier_phone_number']}")
        return
    
    def add_item(self):
        couriers.print_items()

        new_courier = {
            "courier_id" : str(len(self.items)+1),
            "courier_name" : input("Enter new name: ").title(),
            "courier_phone_number" : input("Enter courier's phone number: ")
        }
        self.items.append(new_courier)
        self.save_file()
        print(f"\n{new_courier['courier_name']} - {new_courier['courier_phone_number']} added to the couriers list\n")

    
class Orders(Main_class):

    def __init__(self):
        super().__init__("../data/orders.csv", 
                         [
                             "order_id", 
                          "customer_name", 
                          "customer_address", 
                          "customer_phone", 
                          "courier_id", 
                          "status",
                          "shopping_list" 
                          ]
                         )
    
    def print_items(self, action="\nOrders List"):
        print(action.title())
        if not self.items:
            print(f"{action.strip()} is empty!\n")
            return
        
        for index, item in enumerate(self.items, start=1):
            shopping_list = item["shopping_list"]
            if isinstance(shopping_list, str):
                shopping_list = shopping_list.strip("[]").split(",")
                shopping_list = [prod.strip() for prod in shopping_list]
            
            print(f"{index}. Order #{item['order_id']}\n")
            print(f"\tCustomer: {item['customer_name']}")
            print(f"\tCourier ID: {item['courier_id']}")
            print(f"\tStatus: {item['status']}") 
            print(f"\tItems: {', '.join(shopping_list)}\n")

    def select_products(self):
        print("\nSelect products:")
        products.print_items("Product List")
        
        selected = input("\nEnter product: ").split(",")
        
        try:
            shopping_list = [int(prod.strip()) for prod in selected if prod.strip().isdigit()]
            return shopping_list
        except ValueError:
            print("\nInvalid selection! Try again")
            return self.select_products()

    def add_item(self):
        print("\nCreate new order\n")

        new_order = {
            "order_id": str(len(self.items) + 1),
            "customer_name": input("Name: ").title(),
            "customer_address": input("Address: ").title(),
            "customer_phone": input("Phone number: "),
            "courier_id": input("Enter courier ID: "),
            "status": "Pending",
            "shopping_list": ",".join(map(str, self.select_products()))
        }
        self.items.append(new_order)
        self.save_file()
        print(f"\nOrder #{new_order['order_id']} added for {new_order['customer_name']}!\n")

# menu class

#<@staticmethod> is a decorator that doesnt need .self to be used, it allows to call the methods without creating and instance.

class Menu:
    @staticmethod
    def main_menu():
        print("\nMain Menu\n")
        print("0. Exit")
        print("1. Items Menu")
        print("2. Couriers Menu")
        print("3. Orders Menu")

    @staticmethod
    def item_menu():
        print("\nProducts Menu\n")
        print("0. Back")
        print("1. Check Products")
        print("2. Create New Product")
        print("3. Update Product")
        print("4. Remove Product")

    @staticmethod
    def order_menu():
        print("\nOrders Menu\n")
        print("0. Back")
        print("1. Check Orders")
        print("2. Place Order")
        print("3. Order Status")
        print("4. Update Existing Order")
        print("5. Delete Order")

    @staticmethod
    def courier_menu():
        print("\nCourier Menu\n")
        print("0. Back")
        print("1. Print Courier List")
        print("2. Create New Courier")
        print("3. Update Courier")
        print("4. Delete Courier")

    @staticmethod
    def category():
        print("\nProducts Category\n")
        print("0. Back")
        print("1. Pastry")
        print("2. Sandwich")
        print("3. Coffee")
        print("4. Tea")

# close the class containers

main_class = Main_class()
products = Products()
couriers = Couriers()
orders = Orders()
menu = Menu()
