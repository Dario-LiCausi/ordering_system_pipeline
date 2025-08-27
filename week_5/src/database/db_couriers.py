from database.db_manager import DatabaseManager

db_manager = DatabaseManager()

class DbCouriers(DatabaseManager):
    def __init__(self):
        super().__init__()
        self.create_couriers_table()

    def create_couriers_table(self):
        #create table based on courier.sql
        self.execute_sql_file("/app/src/database/couriers.sql")
    
    def print_couriers(self):
        #print courier list
        self.print_data("couriers")
    
    def select_courier(self):
        #select courier
        return self.select_data("couriers", column="*", action="\nSelect courier:\n")

    def add_courier(self):
        #add courier
        name = input("Courier name: ")
        phone = input("Courier phone: ")
        courier_data = {
            "courier_name": name,
            "courier_phone_number": phone
            }
        # inherit from parent class    
        self.add_data("couriers", courier_data, action="Add courier")

    def edit_courier(self):
        self.print_couriers()
        print("\nSelect the courier to edit:")
        # edit courier
        selected_row = self.select_courier()
        if not selected_row:
            return

        courier_id = selected_row[0]
        current_name = selected_row[1]
        current_phone = selected_row[2]

        new_name = input(f"Edit name (leave blank to keep '{current_name}'): ").strip()
        new_phone = input(f"Edit phone number (leave blank to keep '{current_phone}'): ").strip()
        # create dict with new values
        update_data = {}
        if new_name:
            update_data["courier_name"] = new_name
        if new_phone:
            update_data["courier_phone_number"] = new_phone

        if not update_data:
            print("No changes provided.")
            return

        self.edit_data("couriers", update_data, id_column="courier_id", id_value=courier_id, action="Update courier")

    def delete_courier(self):
        self.print_couriers()
        print("\nSelect the courier to delete:")
        # delete courier
        selected_row = self.select_courier()
        if not selected_row:
            return

        courier_id = selected_row[0]
        self.delete_data("couriers", id_column="courier_id", id_value=courier_id, action="Courier")


