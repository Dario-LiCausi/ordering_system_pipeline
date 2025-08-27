import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

class DatabaseManager:

    def __init__(self):
        # Load the environment variables
        load_dotenv()

        # Initialize DB connection credentials d
        self.DB_HOST = os.getenv("POSTGRES_HOST")
        self.DB_USER = os.getenv("POSTGRES_USER")
        self.DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
        self.DB_NAME = os.getenv("POSTGRES_DB")
        self.DB_PORT = int(os.getenv("POSTGRES_PORT", 5432))

        # Check if all necessary environment variables are set
        if not all([self.DB_HOST, self.DB_USER, self.DB_PASSWORD, self.DB_NAME, self.DB_PORT]):
            raise ValueError("Connection to database not possible, check your credentials in dotenv")
        
        self.conn = self.connect_db()

#connecting to the database
    def connect_db(self):   
        conn = psycopg2.connect(
            host=self.DB_HOST,
            user=self.DB_USER,
            password=self.DB_PASSWORD,
            dbname=self.DB_NAME,
            port=self.DB_PORT
        )
        return conn
#creating tables automatically
    def create_tables(self):
        self.execute_sql_file("/app/src/database/customers.sql")
        self.execute_sql_file("/app/src/database/customer_address.sql")
        self.execute_sql_file("/app/src/database/items.sql")
        self.execute_sql_file("/app/src/database/couriers.sql")
        self.execute_sql_file("/app/src/database/trolley.sql")
        self.execute_sql_file("/app/src/database/orders.sql")

# talking to the database
    def run_query(self, query, params=None, fetch=False):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(query, params)
                if fetch:
                    return cursor.fetchall()
                self.conn.commit()
        except Exception as e:
            print(f"Query failed: {e}")

# entering new data
    def execute_sql_file(self, filename):
        print("Working directory:", os.getcwd())
        print(f"Running {filename}...")
        try:
            with open(filename, 'r') as file:
                sql = file.read()
            self.run_query(sql)
            print(f"Executed {filename} successfully.\n")
        except Exception as e:
            print(f"Failed to execute {filename}: {e}\n")

# printing the data
    def print_data(self, table, column="*"):
        query = f"SELECT {column} FROM {table};"
        rows = self.run_query(query, fetch=True)
        if rows:
            for row in rows:
                cleaned = []
                for field in row:
                    if isinstance(field, str):
                        cleaned.append(field.strip().replace(", ", " "))
                    else:
                        cleaned.append(str(field))
                print(", ".join(cleaned))

# selecting the data
    def select_data(self, table, column="*", action=None):
        print(action.title())
        self.print_data(table, column)
        try:
            select_index = int(input(f"\nSelect option:")) - 1
            
        except ValueError:
            print("Invalid input! Please enter a number.")
            return None
        rows = self.run_query(f"SELECT {column} FROM {table};", fetch=True)
        if rows is None:
            return None
        if 0 <= select_index < len(rows):
            return rows[select_index]
        else:
            print("\nInvalid selection. Try again.")
            return None

# add data
    def add_data(self, table, new_data, action=None):
        if action:
            print(action.title())
        columns = ", ".join(new_data.keys())
        placeholder = ", ".join(['%s'] * len(new_data))
        query = f"INSERT INTO {table}({columns}) VALUES ({placeholder})"
        try:
            self.run_query(query, tuple(new_data.values()))
            print(f"\nNew {action or 'record'} added successfully.\n")
        except Exception as e:
            print(f"Error adding data to {table}: {e}")

    def edit_data(self, table, new_data, id_column, id_value, action=None):
        if action:
            print(action.title())
        column2updt = ", ".join([f"{key} = %s" for key in new_data])
        query = f"UPDATE {table} SET {column2updt} WHERE {id_column} = %s"
        try:
            self.run_query(query, tuple(new_data.values()) + (id_value,))
            print(f"\n{action or 'Record'} updated successfully.\n")
        except Exception as e:
            print(f"Error updating data in {table}: {e}")

    def delete_data(self, table, id_column, id_value, action=None):
        if action:
            print(action.title())

        query = f"DELETE FROM {table} WHERE {id_column} = %s"
        try:
            self.run_query(query, (id_value,))
            print(f"\n{action or 'Record'} deleted successfully.\n")
        except Exception as e:
            print(f"Error deleting data from {table}: {e}")