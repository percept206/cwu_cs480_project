import requests

from cwu_cs480_project.parser import BaseParser
from cwu_cs480_project.database_manager import DatabaseManager
from datetime import datetime


class ParserDB(BaseParser):
    def __init__(self):
        pass

    def parse(self, data):
        pass

    def parse_from_db(self, database, table, primary_key):
        """
        Parses data from the database and converts it into a dictionary.

        Parameters:
            database (DatabaseManager): Database to pull data from
            table (str): Name of the table data is being pulled from
            primary_key (tuple): Tuple in the form of (cik, date).
        Returns:
            dict: Data from database converted into a dictionary.
        """

        pass

    def parse_to_db(self, database, table, primary_key, data):
        """
        Parses a dictionary/tuple given some primary key(s) and pushes it into the database

        Parameters:
            database (DatabaseManager): Database to push data into
            table (str): Name of the table data is being inserted into
            primary_key (tuple): Tuple in the form of (cik, date).
                cik is an integer. date is a string in the format of YYYY-MM-DD.
            data (dict): Data (as a dictionary) that's being pushed into the database. Data is first verified before commit.
        Returns:
            bool: Whether the parse was a success, and an error message in the event parse failed.
        """

        # Make sure date is in valid iso format first
        try:
            datetime.fromisoformat(primary_key[1])
        except ValueError:
            print("date must be in YYYY-MM-DD format.")
            return False, None

        #TODO: Replace "None" values in json with '0'

        formatted_data = data.copy()
        formatted_data["cik"] = primary_key[0]
        # Check if a "date" exists within the data.
        dateExists = [key for key, val in data.items() if "date" in key.lower()]
        if (dateExists):
            if ("exDividendDate" in dateExists):
                formatted_data["dividendDate"] = primary_key[1]
            else:
                formatted_data[dateExists[0]] = primary_key[1]

        columns = ', '.join(formatted_data.keys())
        placeholders = ', '.join(['?'] * len(data))

        insert_sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

        insert_data = tuple(formatted_data[column] for column in data)

        print(insert_sql)
        print(insert_data)

        #try:
        #    database.insert_data(insert_sql, insert_data)
        #    return True, None
        #except Exception as e:
        #    return False, str(e)



#r = requests.get("https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=demo")
#data = r.json()

