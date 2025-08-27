import csv
import os

from classes.main_class import Main_class

# super.__init__ is a method that calls and override the parent class for loading the right csv file.

class Couriers(Main_class):

    def __init__(self):
        super().__init__("/Users/dariolicausi/Documents/Generation/Dario-mini-project/week_5/data/couriers.csv", 
                         [
                             "courier_id", 
                          "courier_name", 
                          "courier_phone_number"
                          ]
                         )
    def print_items(self, action="\nItems Name\n"):
        print(action.title())
        
        if not self.items:
            print(f"{self.items.strip()} is empty!\n")
            return
        
        for index, item in enumerate(self.items, start=1):
            print(f"{index}. {item['courier_name']} - {item['courier_phone_number']}")
        # return
    
    def add_item(self):
        Couriers.print_items(self)

        new_courier = {
            "courier_id" : str(len(self.items)+1),
            "courier_name" : input("Enter new name: ").title(),
            "courier_phone_number" : input("Enter courier's phone number: ")
        }
        self.items.append(new_courier)
        self.save_file()
        print(f"\n{new_courier['courier_name']} - {new_courier['courier_phone_number']} added to the couriers list\n")