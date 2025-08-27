#Dictionaries and lists

products = {
    "Pastry": ["Croissant", "Pan au Chocolat", "Danish", "Brownie", "Carrot Cake", "Pastel de Nata"],
    "Sandwich": ["Egg Mayo", "Coronation Chicken", "Ham And Cheese", "BLT"],
    "Coffee": ["Americano", "Flat White", "Espresso", "Cappuccino", "Mocha", "Latte"],
    "Tea": ["Earl Grey", "English Breakfast", "Green Tea", "Chai Tea", "Chai Latte", "Matcha Latte"]
}

orders = [
    {
        "order_id": "oder #1",
        "customer_name": "John Doe",
        "cutomer_address": "17 St. Anne Road",
        "customer_phone": "07392123456",
        "custmer_city": "London",
        "status": "PREPARING"
    },
    {
        "order_id": "oder #2",
        "customer_name": "Charles Xavier",
        "cutomer_address": "10 Holdborne Street",
        "customer_phone": "0710101010",
        "custmer_city": "Manchester",
        "status": "PREPARING"
    }
]

#creating dashboard

def main_menu():
    print("\nMain Menu\n")
    print("0. Exit")
    print("1. Items Menu")
    print("2. Orders Menu")

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

def category():
    print("0. Back")
    print("1. Pastry")
    print("2. Sandwich")
    print("3. Coffee")
    print("4. Tea")

# Item funcions

#add item

def add_product(prod_category):
    for index, item in enumerate(products[prod_category], start=1):
        print(f"{index}. {item}")

    new_product = input("\nAdd product: ").title()
    
    if new_product in products[prod_category]:
        print(f"\n{new_product} already in {prod_category}!\n")
        
    else:
        products[prod_category].append(new_product)
        print(f"\n{new_product} added to {prod_category}\n")
        category()

#update item by index

def update_product(prod_category):
    for index, item in enumerate(products[prod_category], start=1):
        print(f"{index}. {item}")
    
    update_product_name = int(input("\nChoose the product to update: "))-1

    if 0 <= update_product_name < len(products[prod_category]):
        old_name = products[prod_category][update_product_name]
        new_update = input("Enter the new product name: ").title()
        products[prod_category][update_product_name] = new_update
        print(f"\n{old_name} has been updated to {new_update}!\n")
        
        item_menu()

    else:
        print("\nError, try again!\n")

#delete item

def del_product(prod_category):
    for index, item in enumerate(products[prod_category], start=1):
        print(f"{index}. {item}")
    
    elim_product = int(input('\nReturn the item that you want to delete: '))-1

    if 0 <= elim_product < len(products[prod_category]):
        deleted_item = products[prod_category][elim_product]
        del products[prod_category][elim_product]
        print(f"\n{deleted_item} has been deleted.\n")
        item_menu()
    else:
        print("\nError, try again!\n")

#Orders functions

#New order

def cust_info():
    print()
    order_id = f"order #{len(orders)+1}"
    cust_name = input("Name: ").title()
    cust_phone = input("Phone Number: ").isdigit()
    cust_addr = input("Address: ").title()
    cust_city = input("City or Town: ").title()
    status = "Pending"

    new_order = {
        "order_id": order_id,
        "customer_name": cust_name,
        "cutomer_address": cust_addr,
        "customer_phone": cust_phone,
        "custmer_city": cust_city,
        "status": status
    }
    orders.append(new_order)
    print(f"\nOrder {order_id} added to queue!\n")

#print ord

def print_order(order_id=None):
    if order_id is None:
        if orders:
            order_id = orders[-1]["order_id"]
        else:
            print("\nThere is no orders!\n")
            return

    elif for order in orders:
        print("\nAll Orders:\n")
        for index, order in enumerate(orders, start=1):
            print(f"Order {index}:")
            for key, value in order.items():
                print(f"  {key.replace('_', ' ').title()}: {value}")
            print()
    print("\nOrder not found! Place an order.\n")
     
#Wireframe

while True:
    main_menu()
    choice = input("\nWhat do you want to do? ")

    if choice == "0":
        print("\nGoodbye!\n")
        break
    elif choice == "1":
        
        while True:
            item_menu()
            order_choice = input("\nPick an Option: ")
            if order_choice == "0":
                break
            elif order_choice == "1": #print list
                for category, items in products.items():
                    print(f"\n{category}:\n")
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
                            print("\nInvalid Entry! Try again.")    
 
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
                print("Invalid Entry!")

    elif choice == "2":
        while True:
            order_menu()
            new_order = input("\nPick an Option: ")
            if new_order == "0":
                break
            elif new_order == "1":
                print_order()
            elif new_order == "2":
                cust_info()
            elif new_order == "3":
                print("\nProcessing Orders:")
                if not orders:
                    print("There are no orders to process!")
                else:
                    for index, order in enumerate(orders, start=1):
                        print(f"{index}. Order ID: {order['order_id']}")

                    selected_index = int(input("\nSelect Order: ")) - 1

                    if 0 <= selected_index < len(orders):
                        selected_order = orders[selected_index]
                        print("\nSelected Order Details:")
                        for key, value in selected_order.items():
                            print(f"{key.replace('_', ' ').title()}: {value}")
                    else:
                        print("\nError: Invalid order number. Please try again.")

            
            elif new_order == "4":
                print("update order")
                #print order list with index value
                print_order()
                
                #get user imput for order index value
                '''FOR EACH key-value pair in selected order:
                        GET user input for updated property
                        IF user input is blank:
                            do not update this property
                        ELSE:
                            update the property value with user input'''
            elif new_order == "5":
                print("lorem ipsum")
                #delete order
                #get user input for order index value
                #delete order at index in order list
            else:
                break

    else:
        print("\nWrong entry! Try again\n")  
