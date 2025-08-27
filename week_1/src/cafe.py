# Cafe lists

pastry = ["Croissant", "Pan au Chocolat", "Danish", "Brownie", "Carrot Cake", "Pastel de Nata"]
sandwich = ["Egg Mayo", "Coronation Chicken", "Ham And Cheese", "BLT"]
coffee = ["Americano", "Flat White", "Espresso", "Cappuccino", "Mocha", "Latte"]
tea = ["Earl Grey", "English Breakfast", "Green Tea", "Chai Tea", "Chai Latte", "Matcha Latte"]

"""
This method doesnt update the super list!

products = []
products.extend(coffee)
products.extend(sandwich)
products.extend(pastry)
products.extend(tea)"""

#This Does!
#Super list function that updates the main list

def mlproducts():
    return pastry + coffee + sandwich + tea

'''
x = ('apple', 'banana', 'cherry')
y = enumerate(x)
   
for x in "banana":
print(x)
'''
# Defining function to call enumerated lists in action
# Function that enumerates the list at every modification and i can call back when i need to print the whole list.

def print_products():
    products = mlproducts()
    print("\nProduct List:\n")
    for index, item in enumerate(products, start=1):
        print(f"{index}. {item}")

def print_pastry():
    
    print("\nPastry List:\n")
    for index, item in enumerate(pastry, start=1):
        print(f"{index}. {item}")

def print_sandwich():
    
    print("\nSandwich List:\n")
    for index, item in enumerate(sandwich, start=1):
        print(f"{index}. {item}")

def print_coffee():
    
    print("\nCoffee List:\n")
    for index, item in enumerate(coffee, start=1):
        print(f"{index}. {item}")

def print_tea():
    
    print("\nTea List:\n")
    for index, item in enumerate(tea, start=1):
        print(f"{index}. {item}")

# Defining functions

#Clear Screen
'''
nt = windows, posix = linux/mac
cls clear screen in win
clear does the same for the others
'''
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main menu
def main_menu():
    print("\nMain Menu:")
    print("\n0. Exit")
    print("1. Products Menu")

    option_mm = input("\nWhat do you want to do today? ")

    if option_mm == "0":
        print("Closing the app, goodbye!")
        exit()
    elif option_mm == "1":
        products_menu()
    else:
        print("Invalid entry!")
        main_menu()

# Secondary menu    
def products_menu():
    print("\nProducts Menu:\n")
    print("0. Go Back")
    print("1. View Products")
    print("2. Add New Product")
    print("3. Update Existing Product")
    print("4. Delete Product")
    print("5. Clear Screen")

    option_pm = input("\nSelect an option: ")

    if option_pm == "0":
        main_menu()
    elif option_pm == "1":
        print_products()
        products_menu()
    elif option_pm == "2":
        category() 
    elif option_pm == "3":
        edit()
    elif option_pm == "4":
        remove()
    elif option_pm == "5":
        clear()    
    else:
        print("Invalid entry!")
        products_menu()

# Add item to list
def category():
    print("\n0. Go Back")
    print("1. Pastry")
    print("2. Sandwich")
    print("3. Coffee")
    print("4. Tea")
    print("5. Clear Screen")
    
    cat_choice = input("\nWhat category do you want to update? ")
    
    if cat_choice == "0":
        products_menu()
    elif cat_choice == "1":
        print_pastry()
        new_item = input("\nAdd product: ").title()
        if new_item in pastry:
            print(f"{new_item} already in Pastry!")
            category()
        else:
            pastry.append(new_item)
            print(f"{new_item} added to Pastry!")
            products_menu()
    elif cat_choice == "2":
        print_sandwich()
        new_item = input("\nAdd product: ").title()
        if new_item in sandwich:
            print(f"{new_item} already in Sandwich!")
            category()
        else:
            sandwich.append(new_item)
            print(f"{new_item} added to Sandwich!")
            products_menu()
    elif cat_choice == "3":
        print_coffee()
        new_item = input("\nAdd product: ").title()
        if new_item in coffee:
            print(f"{new_item} already in Coffee!")
            category()
        else:
            coffee.append(new_item)
            print(f"{new_item} added to Coffee!")
            products_menu()
    elif cat_choice == "4":
        print_tea()
        new_item = input("\nAdd product: ").title()
        if new_item in tea:
            print(f"{new_item} already in Pastry!")
            category()
        else:    
            tea.append(new_item)
            print(f"{new_item} added to Tea!")
            products_menu()
    elif cat_choice == "5":
        clear() 
    else:
        print("Invalid entry!")
        category()

#Edit item in a category
# for index, item in enumerate(my_list, start=1):
    #print(f"{index}. {item}")
'''thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)'''

def edit():
    print("\n0. Go Back")
    print("1. Pastry")
    print("2. Sandwich")
    print("3. Coffee")
    print("4. Tea")
    print("5. Clear Screen")

    edit = input("\nChose a gategory where to edit your item ")


    if edit == "0":
        products_menu()
    elif edit == "1":
        print()
        for index,item in enumerate(pastry, start=0):
            print(f"{index}. {item}")
        item_edit = int(input("\nReturn the index of the item that you want to update "))
        old_item = pastry[item_edit]
        item_replace = input("\nWhat do you want to replace it with? ").title()
        pastry[item_edit] = item_replace
        print(f"\n{old_item} had been replaced with {item_replace}!" )
        products_menu()
    elif edit == "2":
        print()
        for index,item in enumerate(pastry, start=1):
            print(f"{index}. {item}")
        item_edit = int(input("\nReturn the index of the item that you want to update "))
        old_item = sandwich[item_edit]
        item_replace = input("\nWhat do you want to replace it with? ").title()
        sandwich[item_edit] = item_replace
        print(f"\n{old_item} had been replaced with {item_replace}!" )
        products_menu()
    elif edit == "3":
        print()
        for index,item in enumerate(coffee, start=1):
            print(f"{index}. {item}")
        item_edit = int(input("\nReturn the index of the item that you want to update "))
        old_item = coffee[item_edit]
        item_replace = input("\nWhat do you want to replace it with? ").title()
        coffee[item_edit] = item_replace
        print(f"\n{old_item} had been replaced with {item_replace}!" )
        products_menu()
    elif edit == "4":
        print()
        for index,item in enumerate(tea, start=1):
            print(f"{index}. {item}")
        item_edit = int(input("\nReturn the index of the item that you want to update "))
        old_item = tea[item_edit]
        item_replace = input("\nWhat do you want to replace it with? ").title()
        tea[item_edit] = item_replace
        print(f"\n{old_item} had been replaced with {item_replace}!" )
        products_menu()
    elif edit == "5":
        clear() 
    else:
        print("Wrong entry! ")
        edit()


# Remove item from category 
def remove():
    print("\n0. Go Back")
    print("1. Pastry")
    print("2. Sandwich")
    print("3. Coffee")
    print("4. Tea")
    print("5. Clear Screen")
    
    remove = input("\nWhat category do you want to remove from? ")
    
    if remove == "0":
        products_menu()
    elif remove == "1":
        print()
        print_pastry()
        del_item = input("Remove product: ").title()
        if del_item in pastry:
            pastry.remove(del_item)
            print(f"{del_item} removed from Pastry!")
            products_menu()
        else:
            print(f"{del_item} not found in Pastry!")
            remove()
    elif remove == "2":
        print()
        print_sandwich()
        del_item = input("Remove product: ").title()
        if del_item in sandwich:
            sandwich.remove(del_item)
            print(f"{del_item} removed from Sandwich!")
            products_menu()
        else:
            print(f"{del_item} not found in Sandwich!")
            remove()
    elif remove == "3":
        print()
        print_coffee()
        del_item = input("Remove product: ").title()
        if del_item in coffee:
            coffee.remove(del_item)
            print(f"{del_item} removed from Coffee!")
            products_menu()
        else:
            print(f"{del_item} not found in Coffee!")
            remove()
    elif remove == "4":
        print()
        print_tea()
        del_item = input("Remove product: ").title()
        if del_item in tea:
            tea.remove(del_item)
            print(f"{del_item} removed from Tea!")
            products_menu()
        else:
            print(f"{del_item} not found in Tea!")
            remove()
    elif remove == "5":
        clear() 
    else:
        print("Invalid entry!")
        remove()

main_menu()

