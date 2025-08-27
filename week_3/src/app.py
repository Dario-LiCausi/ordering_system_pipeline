from functions import *
     
#Wireframe

while True:
    main_menu()
    choice = input("\nSelect option: ")

    if choice == "0":#quit
        print("\nGoodbye!\n")
        break
    elif choice == "1": #products menu
        while True:
            item_menu()
            order_choice = input("\nSelect option: ")
            if order_choice == "0":
                break
            elif order_choice == "1": #print list
                for cat_name, items in products.items():
                    print(f"\n{cat_name}:\n")
                    for index, item in enumerate(items, start=1):
                        print(f"{index}. {item}")
                print()  
            elif order_choice == "2": #New Product menu
                print ("\nCreate New Product\n ")
                category()
                while True:
                    
                    cat_choice = input("\nChose a category: ")    
                    print()

                    if cat_choice == "0":
                            break
                    elif cat_choice == "1":
                        add_product("Pastry")
                        
                    elif cat_choice == "2":
                        add_product("Sandwich")

                    elif cat_choice == "3":
                        add_product("Coffee")

                    elif cat_choice == "4":
                        add_product("Tea")
                    else:
                        print("\nTry again:")    
 
            elif order_choice == "3": #Update product
                print ("\nUpdate Product\n ")
                category()
                while True:
                    cat_choice = input("\nChose a category: ")    
                    print()
                    if cat_choice == "0":
                        break
                    elif cat_choice == "1":
                        update_product("Pastry")
                    elif cat_choice == "2":
                        update_product("Sandwich")
                    elif cat_choice == "3":
                        update_product("Coffee")
                    else:
                        cat_choice == "4"
                        update_product("Tea")
        
            elif order_choice == "4": #Delete product
                print ("\nRemove Product\n ")
                category()
                while True:
                    cat_choice = input("\nChose a category: ")    
                    print()
                    
                    if cat_choice == "0":
                        break
                    elif cat_choice == "1":
                        del_product("Pastry")
                    elif cat_choice == "2":
                        del_product("Sandwich")
                    elif cat_choice == "3":
                        del_product("Coffee")
                    else:
                        cat_choice == "4"
                        del_product("Tea")

            else:
                print("Try again: ")
    elif choice == "2": #courier menu
        while True:
            courier_menu()
            courier_selection = input("\nSelect an option: ")
            if courier_selection == "0":
                break
            elif courier_selection == "1":
                print_courier_list()
            elif courier_selection == "2":
                new_courier()
            elif courier_selection == "3":
                update_courier()
            elif courier_selection == "4":
                delete_courier()
            else:
                break
    elif choice == "3":#orden menu
        while True:
            order_menu()
            new_order = input("\nSelect an option: ")
            if new_order == "0":
                break
            elif new_order == "1":
                print_orders()
            elif new_order == "2":
                cust_info()
            elif new_order == "3":
                update_status()
            elif new_order == "4":
                update_order_details()
            elif new_order == "5":
                delete_order()
            else:
                break
    else:
        print("\nTry again\n")  
