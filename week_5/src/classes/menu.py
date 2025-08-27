# from classes.main_class import Main_class


#<@staticmethod> is a decorator that doesnt need .self to be used, it allows to call the methods without creating and instance.

class Menu:
    @staticmethod
    def main_menu():
        print("\nMain Menu\n")
        print("0. Exit")
        print("1. Items Menu")
        print("2. Couriers Menu")
        print("3. Orders Menu")
        print("4. Clear Screen")

    @staticmethod
    def item_menu():
        print("\nProducts Menu\n")
        print("0. Back")
        print("1. Check Products")
        print("2. Create New Product")
        print("3. Update Product")
        print("4. Remove Product")
        print("5. Clear Screen")

    @staticmethod
    def order_menu():
        print("\nOrders Menu\n")
        print("0. Back")
        print("1. Check Orders")
        print("2. Place Order")
        print("3. Order Status")
        print("4. Update Existing Order")
        print("5. Delete Order")
        print("6. Clear Screen")

    @staticmethod
    def courier_menu():
        print("\nCourier Menu\n")
        print("0. Back")
        print("1. Print Courier List")
        print("2. Create New Courier")
        print("3. Update Courier")
        print("4. Delete Courier")
        print("5. Clear Screen")

    @staticmethod
    def category():
        print("\nProducts Category\n")
        print("0. Back")
        print("1. Pastry")
        print("2. Sandwich")
        print("3. Coffee")
        print("4. Tea")
        print("5. Clear Screen")

