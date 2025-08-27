# importing classes and initialising them

from classes.products import Products
from classes.couriers import Couriers
from classes.orders import Orders
from classes.menu import Menu
from classes.main_class import Main_class
from database.db_manager import DatabaseManager
from database.db_couriers import DbCouriers
# from database.db_orders import DbOrders
from database.db_items import DbItems

main_class = Main_class()
products = Products()
couriers = Couriers()
orders = Orders()
menu = Menu()

db_manager = DatabaseManager()
db_couriers = DbCouriers()
db_items = DbItems()
# db_orders = DbOrders()


# Wireframe
# core structure of the app, every selection calls back to a different function in main_class.py

while True:
    menu.main_menu()
    choice = input("\nSelect option: ")
    if choice == "0":#quit
        print("\nGoodbye!\n")
        break
    elif choice == "1": #products menu
        while True:
            menu.item_menu()
            prod_choice = input("\nSelect option: ")
            print()
            if prod_choice == "0":
                break
            elif prod_choice == "1": #print list
                db_items.print_item()  
            elif prod_choice == "2": #New Product menu
                print ("\nCreate New Product\n ")
                db_items.add_item()   
            elif prod_choice == "3": #Update product
                print ("\nUpdate Product\n ")
                db_items.edit_item()
            elif prod_choice == "4": #Delete product
                print ("\nRemove Product\n ")
                db_items.delete_item()
            elif prod_choice == "5": #Clear screen
                main_class.clear()
            else:
                print("Try again: ")
    elif choice == "2": #courier menu
        while True:
            menu.courier_menu()
            courier_selection = input("\nSelect an option: ")
            if courier_selection == "0":
                break
            elif courier_selection == "1":
                db_couriers.print_couriers()
            elif courier_selection == "2":
                db_couriers.add_courier()
            elif courier_selection == "3":
                db_couriers.edit_courier()
            elif courier_selection == "4":
                db_couriers.delete_courier()
            elif courier_selection == "5": #Clear screen
                main_class.clear()
            else:
                break
    elif choice == "3":#orden menu
        while True:
            menu.order_menu()
            order_choice = input("\nSelect an option: ")
            if order_choice == "0":
                break
            elif order_choice == "1":
                orders.print_items("Orders:\n ")
            elif order_choice == "2":
                orders.add_item()
            elif order_choice == "3":
                orders.update_status("order")
            elif order_choice == "4":
                orders.edit_item("order")
            elif order_choice == "5":
                orders.delete_item("order")
            elif order_choice == "6": #Clear screen
                main_class.clear()    
            else:
                break
    elif choice == "4": #Clear screen
        main_class.clear()
    else:
        print("\nTry again\n")  
