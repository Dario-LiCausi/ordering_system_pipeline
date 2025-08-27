# from database.db_manager import DatabaseManager

# db_manager = DatabaseManager()

# class DbOrders(DatabaseManager):
#     def __init__(self):
#         super().__init__()
#         self.create_orders_table()

# def create_orders_table(self):
#         #create table based on orders.sql
#         self.execute_sql_file("/app/src/database/orders.sql")

# def create_customer_table(self):
#         #customer table
#         self.execute_sql_file("/app/src/database/cutomer_customer.sql")


# def create_address_table(self):
#         #address table
#         self.execute_sql_file("/app/src/database/cutomer_address.sql")

# def print_orders(self):
#         #print orders list
#         self.print_data("orders")

# def select_orders(self):
#         #select order
#         return self.select_data("couriers", column="*", action="\nSelect order:\n")

# def add_order(self):
#         #add order
#         ("\nPlace new order\n")
#         name = input("Customer name: ").title()
#         try:
#                 phone = int(input("Phone number: "))
#                 if not isinstance
#                 return
#         except ValueError:
#                 print("Error: Invalid phone number!")
#                 return
#         item_data = {
#                 "customer_name": name
#                 "cutomer_phone_number": phone
#         }
#         self.add_data("customer", customer_data, action="Add Info")


#         street = input("Street: ").title()
#         house_number = input ("House number: ")
#         city = input ("City / Town: ").title()
#         post_code = input ("Post code: ")
#         item_data = {
#                 "house_numb": house_number,
#                 "street": street,
#                 "city": city,
#                 "post_code": post_code
#         }
#         self.add_data("customer_address", address_data, action="Add Address")

#         status =
#         courier =
#         order_data = {
#             "courier_name": name,
#             "courier_phone_number": phone
#             }
#         # inherit from parent class    
#         self.add_data("couriers", courier_data, action="Add courier")

# def delete_order(self):
#         # delete order
#         self.print_order()
#         print("Choose the order to delete: ")

#         selected_row = self.select_order()
#         if not selected_row:
#             return

#         item_id = selected_row[0]
#         self.delete_order("order", id_column="order_id", id_value=order_id, action="Order")