from functions import Products, Couriers, Orders, Menu

# Create instances
menu = Menu()
products = Products()
couriers = Couriers()
orders = Orders()
     
# Wireframe
# core structure of the app, every selection calls back to a different function for functions.py

while True:
    menu.main_menu()
    choice = input("\nSelect option: ")
    if choice == "0":#quit
        print("\nGoodbye!\n")
        break
    elif choice == "1": #products menu
        while True:
            menu.item_menu()
            order_choice = input("\nSelect option: ")
            if order_choice == "0":
                break
            elif order_choice == "1": #print list
                products.print_items("\nProducts\n")  
            elif order_choice == "2": #New Product menu
                print ("\nCreate New Product\n ")
                products.add_item()   
            elif order_choice == "3": #Update product
                print ("\nUpdate Product\n ")
                products.edit_item("product")
            elif order_choice == "4": #Delete product
                print ("\nRemove Product\n ")
                products.delete_item("product")
            else:
                print("Try again: ")
    elif choice == "2": #courier menu
        while True:
            menu.courier_menu()
            courier_selection = input("\nSelect an option: ")
            if courier_selection == "0":
                break
            elif courier_selection == "1":
                couriers.print_items("\nCouriers List:\n ")
            elif courier_selection == "2":
                couriers.add_item()
            elif courier_selection == "3":
                couriers.edit_item("courier")
            elif courier_selection == "4":
                couriers.delete_item("courier")
            else:
                break
    elif choice == "3":#orden menu
        while True:
            menu.order_menu()
            new_order = input("\nSelect an option: ")
            if new_order == "0":
                break
            elif new_order == "1":
                orders.print_items("Orders:\n ")
            elif new_order == "2":
                orders.add_item()
            elif new_order == "3":
                orders.update_status("order")
            elif new_order == "4":
                orders.edit_item("order")
            elif new_order == "5":
                orders.delete_item("order")
            else:
                break
    else:
        print("\nTry again\n")  
