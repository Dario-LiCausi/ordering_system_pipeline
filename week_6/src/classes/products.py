import csv
import os

from classes.main_class import Main_class
# super.__init__ is a method that calls and override the parent class for loading the right csv file.

class Products(Main_class):
    def __init__(self):
        super().__init__("/Users/dariolicausi/Documents/Generation/Dario-mini-project/week_5/data/products_list.csv", 
                         [
                             "category", 
                             "item", 
                             "price"
                             ]
                         )

# creates and empty dictionary that stores the items mapping between the actual index number and the printed index number (so it starts from 1).
# sorted() is a function that extracts the values of the category key and makes them unique.
# douple for loop, the first one iterats through the category keys and the second one iterates through the items.
# it's a way to format and organize the products dictionary when printed.
# return the index mapping value.
    def print_items(self, action="\nMenu\n"):
        print(action.title())

        if not self.items:
            print(f"{str(action).strip()} is empty!\n")
            return
        
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
