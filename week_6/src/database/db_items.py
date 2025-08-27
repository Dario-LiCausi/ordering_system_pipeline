from database.db_manager import DatabaseManager

db_manager = DatabaseManager()

class DbItems(DatabaseManager):
    def __init__(self):
        super().__init__()
        self.create_item_table()

    def create_item_table(self):
        #create table based on .sql
        self.execute_sql_file("/app/src/database/items.sql")

    def print_item(self):
        #print items list
        self.print_data("items")

    def select_item(self):
        #select items
        return self.select_data("items", column="*", action="\nSelect item:\n")

    def add_item(self):
        #ux practicallity
        self.print_item()
        print("\nCreate a new product\n")
        #add item
        category = input("Enter category: ").title()
        item = input("Enter item: ").title()
            
        try:
            price = float(input("Enter price: "))
            if price < 0:
                print("Error: Invalid entry")
                return
        except ValueError:
            print("Error: Price must be a number - 0.00.")
            return

    # 2 decimals
        price = float(f"{price:.2f}")

        item_data = {
            "category": category,
            "item": item,
            "price": price
            }
        # inherit from parent class    
        self.add_data("items", item_data, action="Add Item")

    def edit_item(self):
        # edit item
        self.print_item()

        print("\nChoose the product to update: ")
        selected_row = self.select_item()
        if not selected_row:
            return

        item_id = selected_row[0]
        current_category = selected_row[1]
        current_name = selected_row[2]
        current_price = selected_row[3]

        new_category = input(f"Edit category (leave blank to keep '{current_category}'): ").title().strip()
        new_name = input(f"Edit name (leave blank to keep '{current_name}'): ").title().strip()
        new_price_input = input(f"Edit price (leave blank to keep '{current_price}'): ").strip()
        
        # create dict with new values
        update_data = {}
        if new_category:
            update_data["category"] = new_category
        if new_name:
            update_data["item"] = new_name
        if new_price_input:
            try:
                new_price = float(new_price_input)
                if new_price < 0:
                    print("Error: Invalid entry")
                    return
                # Format to 2 decimals
                update_data["price"] = float(f"{new_price:.2f}")
            except ValueError:
                print("Error: Price must be a number - 0.00.")
                return

        if not update_data:
            print("No changes provided.")
            return

        self.edit_data("items", update_data, id_column="item_id", id_value=item_id, action="Update Product")
    
    def delete_item(self):
        # delete item
        self.print_item()
        print("Choose the product to delete: ")

        selected_row = self.select_item()
        if not selected_row:
            return

        item_id = selected_row[0]
        self.delete_data("items", id_column="item_id", id_value=item_id, action="Item")