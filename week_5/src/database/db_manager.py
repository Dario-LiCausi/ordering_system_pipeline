import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

# DB_HOST = os.getenv("POSTGRES_HOST")
# DB_USER = os.getenv("POSTGRES_USER")
# DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
# DB_NAME = os.getenv("POSTGRES_DB")
# DB_PORT = int(os.getenv("POSTGRES_PORT", 5432))

class DatabaseManager:

    def __init__(self):
        # Load the environment variables
        load_dotenv()

        # Initialize DB connection parameters from environment variables
        self.DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
        self.DB_USER = os.getenv("POSTGRES_USER", "postgres")
        self.DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "mydbpsw")
        self.DB_NAME = os.getenv("POSTGRES_DB", "postgres")
        self.DB_PORT = int(os.getenv("POSTGRES_PORT", 5432))

        # Check if all necessary environment variables are set
        if not all([self.DB_HOST, self.DB_USER, self.DB_PASSWORD, self.DB_NAME, self.DB_PORT]):
            raise ValueError("Connection to database not possible, check your credentials in dotenv")
        
        self.conn = self.connect_db()
    # def __init__(self):
    #     if not all([DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT]):
    #         raise ValueError("Connection to database not possible, check your credentials in dotenv")
    #     self.conn = self.connect_db()

    def connect_db(self):
        conn = psycopg2.connect(
            host=self.DB_HOST,
            user=self.DB_USER,
            password=self.DB_PASSWORD,
            dbname=self.DB_NAME,
            port=self.DB_PORT
        )
        return conn

    def create_tables(self):
        self.execute_sql_file("/app/src/database/customers.sql")
        self.execute_sql_file("/app/src/database/customer_address.sql")
        self.execute_sql_file("/app/src/database/items.sql")
        self.execute_sql_file("/app/src/database/couriers.sql")
        self.execute_sql_file("/app/src/database/trolley.sql")
        self.execute_sql_file("/app/src/database/orders.sql")

    def run_query(self, query, params=None, fetch=False):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(query, params)
                if fetch:
                    return cursor.fetchall()
                self.conn.commit()
        except Exception as e:
            print(f"Query failed: {e}")

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





# import os
# import psycopg2
# from dotenv import load_dotenv

# load_dotenv()

# DB_HOST = os.getenv("POSTGRES_HOST")
# DB_USER = os.getenv("POSTGRES_USER")
# DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
# DB_NAME = os.getenv("POSTGRES_DB")
# DB_PORT = int(os.getenv("POSTGRES_PORT", 5432))

# class Database_manager():

#     def __init__(self):
#         self.conn = self.connect_db()
        
#         if not all([DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT]):
#             raise ValueError("Connection to database not possible, check your credentials in dotenv")

#     def connect_db(self):
#         print(f"Connecting to DB: host={DB_HOST}, user={DB_USER}, dbname={DB_NAME}, port={DB_PORT}")
#         conn = psycopg2.connect(
#             host=DB_HOST,
#             user=DB_USER,
#             password=DB_PASSWORD,
#             dbname=DB_NAME,
#             port=DB_PORT
#         )
#         return conn

#     def create_tables(self):
#         execute_sql_file("/app/src/database/customers.sql")
#         execute_sql_file("/app/src/database/customer_address.sql")
#         execute_sql_file("/app/src/database/items.sql")
#         execute_sql_file("/app/src/database/couriers.sql")
#         execute_sql_file("/app/src/database/trolley.sql")
#         execute_sql_file("/app/src/database/orders.sql")

#     def run_query(self, query, params=None, fetch=False):
#         conn = self.connect_db()
#         if conn is None:
#             print("Failed to connect to the database.")
#             return None

#         try:
#             with conn.cursor() as cursor:
#                 cursor.execute(query, params)
#                 if fetch:
#                     return cursor.fetchall()
#                 conn.commit()
#         except Exception as e:
#             print(f"Query failed: {e}")
#         finally:
#             conn.close()

#     def execute_sql(self, filename):
#         print("Working directory:", os.getcwd())
#         print(f"Running {filename}...")

#         try:
#             with open(filename, 'r') as file:
#                 sql = file.read()

#             self.run_query(sql)
#             print(f"Executed {filename} successfully.\n")

#         except Exception as e:
#             print(f"Failed to execute {filename}: {e}\n")

#     def print_data(self, table, column = "*"):
#         query = f"SELECT {column} FROM {table};"
#         rows = self.run_query(query, fetch = True)
#         if rows:
#             for index, row in enumerate(row, 1):
#                 print(f"{index}. {row}")
            
#     def select_data(self, table, column = "*", action = None):
#         print(action.title())
#         self.print_data(table, column)

#         try:
#             select_index = int(input(f"\nSelect option: ")) -1
#         except ValueError:
#             print("Invalid input! Please enter a number.")
#             return None

#         query = f"SELECT {column} FROM {table};"
#         rows = self.run_query(query, fetch=True)

#         if rows is None:
#             return None

#         if 0 <= select_index < len(rows):
#             return rows[select_index]
#         else:
#             print("\nInvalid selection. Try again.")
#             return None
        
#     def add_data(self, table, new_data, action = None):
#         if action:
#             print(action.title())
        
#         self.print_data(table, column)

#         columns = ", ".join(new_data.keys())
#         placeholder = ", ".join(['%s'] * len(new_data))
#         query = f"INSERT INTO {table}({columns}) VALUES ({placeholder})"
#         try:
#             self.run_query(query, tuple(new_data.values()))
#             print(f"\nNew {action or 'record'} added successfully.\n")
#         except Exception as e:
#             print(f"Error adding data to {table}: {e}")

#     def edit_data(self, table, new_data, id_column, id_value, action=None):
#         if action:
#             print(action.title())

#         column2updt = ", ".join([f"{key} = %s" for key in new_data])
#         query = f"UPDATE {table} SET {column2updt} WHERE {id_column} = %s"
#         try:
#             self.run_query(query, tuple(new_data.values()) + (id_value,))
#             print(f"\n{action or 'Record'} updated successfully.\n")
#         except Exception as e:
#             print(f"Error updating data in {table}: {e}")

#     # def delete_data():

            