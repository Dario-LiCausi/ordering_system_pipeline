from database.db_manager import DatabaseManager

db_manager = DatabaseManager()

class DbOrders(DatabaseManager):
    def __init__(self):
        super().__init__()
        self.create_orders_table()

def create_couriers_table(self):
        #create table based on orders.sql
        self.execute_sql_file("/app/src/database/orders.sql")   

def print_orders(self):
        #print orders list
        self.print_data("orders")

def select_orders(self):
        #select order
        return self.select_data("couriers", column="*", action="\nSelect order:\n")

def add_order(self):
        #add order
        name = input("Customer name: ")
        phone = input("Courier phone: ")
        courier_data = {
            "courier_name": name,
            "courier_phone_number": phone
            }
        # inherit from parent class    
        self.add_data("couriers", courier_data, action="Add courier")