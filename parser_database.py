from cwu_cs480_project.parser import BaseParser
from cwu_cs480_project.database_manager import DatabaseManager

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
            data (dict): Data (as a dictionary) that's being pushed into the database. Data is first verified before commit.
        Returns:
            bool: Whether the parse was a success, and an error message in the event parse failed.
        """
        pass