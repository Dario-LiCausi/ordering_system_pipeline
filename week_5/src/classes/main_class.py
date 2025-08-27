# import

import os
import csv
# import psycopg2
# from .env import load_dotenv

# parent class.
# OOP - main class to set the reles of all the main and repetetive functions/methods.
# load/read and write/save data in the respective csv files.
# if fielname is not found it is assigned to an empty list

class Main_class:
    
    def __init__(self, file_path="default.csv", fieldnames=None):
        self.file_path = file_path
        self.fieldnames = fieldnames if fieldnames else []
        self.items = self.load_file()

        print(f"DEBUG: Start Loading {self.file_path}")
# load_file if there is a file, it converts it (the csv file) in a dictionary and returns it
# if the file doesnt exists it returns in a empty list []

    # def load_file(self):
    #     file_path = os.path.join(os.path.dirname(__file__), self.file_path)
    #     if not os.path.exists(file_path):  
    #         return []
    #     with open(file_path, "r", newline="") as file:
    #         reader = csv.DictReader(file)
    #         return list(reader)

    def load_file(self):

        print(f"DEBUG: Attempting to load {self.file_path}")

        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, "r", newline="") as file:
            reader = csv.DictReader(file)
            return list(reader)
        
            print("DEBUG: Loaded Data from CSV =", data)
        return data

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

    def print_items(self, action = "\nItems Name\n"):
        print(action.title())
        if not self.items:
            print(f"{action.strip()if isinstance(action, str) else action} is empty!\n")
            return
        
        for index, item in enumerate(self.items, start=1):
            value = next(iter(item.values()), "No Data")
            print(f"{index}. {value}")
            # print(f"{index}. {item_name.replace('_', ' ')}")

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
        # <ifistance> check if the object is a string so i can apply .title() if it is not, it skips title and doesnt show error
        print(f"\nUpdating {action.title() if isinstance(action, str) else action} Details\n")
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


#clear screen

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
