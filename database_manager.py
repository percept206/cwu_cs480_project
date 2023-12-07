import sqlite3
from sqlite3 import Error
class DatabaseManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None
        self.connect()

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_file)
            self.connection.row_factory = sqlite3.Row
        except Error as e:
            print(e)

    def is_connected(self):
        try:
            self.connection.cursor()
            return True
        except Exception as e:
            return False

    def create_table(self, create_table_sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
        except Error as e:
            print(e)
    def insert_data(self, insert_sql, data):
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_sql, data)
            self.connection.commit()
        except Error as e:
            print(e)

    def query_data(self, query, data):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, data)
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(e)
    def close(self):
        if self.connection:
            self.connection.close()


#database = "financial_db.db"
#db_manager = DatabaseManager(database)

#query = "SELECT cik FROM Company"
#companies = db_manager.query_data(query)
#for company in companies:
#    print(company)