import requests

from parser import BaseParser
from database_manager import DatabaseManager
from datetime import datetime

from parser_json import ParserJSON


class ParserDB(BaseParser):
    def __init__(self):
        pass

    def parse(self, data):
        pass

    def __parse_from_db__(self, database, table, primary_key, date_column_name):
        """
        Parses data from the database and converts it into a dictionary.

        Parameters:
            database (DatabaseManager): Database to pull data from.
            table (str): Name of the table data is being pulled from.
            primary_key (tuple): Tuple in the form of (cik, date).
            date_column_name (str): Name of the date column within the database.
        Returns:
            data_dict: Data from database converted into a dictionary.
        """

        # Make sure date is in valid iso format first
        try:
            datetime.fromisoformat(primary_key[1])
        except ValueError:
            print("date must be in YYYY-MM-DD format.")
            return None

        query = f"SELECT * FROM {table} WHERE cik = ? AND {date_column_name} = ?"

        rows = database.query_data(query, primary_key)

        data_dict = {}
        if len(rows) > 1:
            raise ValueError("More than one row returned for the given primary keys!")
        inspect = rows[0]
        data_dict = {k: inspect[k] for k in inspect.keys()}

        #print(data_dict)

        return data_dict

    def __parse_to_db__(self, database, table, primary_key, data):
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

        formatted_data = data.copy()
        formatted_data["cik"] = primary_key[0]
        # Check if a "date" exists within the data.
        date_exists = [key for key, val in data.items() if "date" in key.lower()]
        if date_exists:
            if "exDividendDate" in date_exists:
                formatted_data["dividendDate"] = primary_key[1]
            else:
                formatted_data[date_exists[0]] = primary_key[1]

        columns = ', '.join(formatted_data.keys())
        placeholders = ', '.join(['?'] * len(data))

        insert_sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

        insert_data = tuple(formatted_data[column] for column in data)

        #print(insert_sql)
        #print(insert_data)

        try:
            database.insert_data(insert_sql, insert_data)
            return True, None
        except Exception as e:
            return False, str(e)

    def parse_into_monthly_time_series(self, database, primary_key, data):
        """
        Parses monthly time series information into the database. Probably should be its own class.

        Parameters: database (databaseManager): Database to push data into primary_key (tuple): Tuple in the form of
        (cik, date). cik is an integer. date is a string in the format of YYYY-MM-DD. data (dict): Data (as a
        dictionary) that's being pushed into the database. Data is first verified before commit. Returns: bool:
            Whether the parse was a success, and an error message in the event parse failed.
        """

        # First check and make sure we're on the right file.
        if data["Meta Data"] is None or "Monthly" not in data["Meta Data"]["1. Information"]:
            return False, None

        db_table = "MonthlyTimeSeries"
        json_table = "Monthly Time Series"

        try:
            # primary_key[1]
            list(data[json_table][primary_key[1]].values())
        except KeyError:
            print(
                "ERROR: Date provided is not valid or found within the data. Please provide a valid date in the form of YYYY-MM-DD.")
            return False, None
        processedData = {"cik": primary_key[0], "date": primary_key[1]}
        processedData["open"] = data[json_table][primary_key[1]]["1. open"]
        processedData["high"] = data[json_table][primary_key[1]]["2. high"]
        processedData["low"] = data[json_table][primary_key[1]]["3. low"]
        processedData["close"] = data[json_table][primary_key[1]]["4. close"]
        processedData["volume"] = data[json_table][primary_key[1]]["5. volume"]

        return self.__parse_to_db__(database, db_table, primary_key, processedData)

    def parse_into_daily_time_series(self, database, primary_key, data):
        """
        Parses daily time series information into the database.

        Parameters:
            database (databaseManager): Database to push data into
            primary_key (tuple): Tuple in the form of (cik, date).
                cik is an integer. date is a string in the format of YYYY-MM-DD.
            data (dict): Data (as a dictionary) that's being pushed into the database. Data is first verified before commit.
        Returns:
            bool: Whether the parse was a success, and an error message in the event parse failed.
        """
        # First check and make sure we're on the right file.
        if (data["Meta Data"] == None or "Daily" not in data["Meta Data"]["1. Information"]):
            return False, None

        db_table = "DailyTimeSeries"
        json_table = "Time Series (Daily)"

        try:
            # primary_key[1]
            list(data[json_table][primary_key[1]].values())
        except KeyError:
            print(
                "ERROR: Date provided is not valid or found within the data. Please provide a valid date in the form "
                "of YYYY-MM-DD.")
            return False, None
        processed_data = {"cik": primary_key[0], "date": primary_key[1],
                          "open": data[json_table][primary_key[1]]["1. open"],
                          "high": data[json_table][primary_key[1]]["2. high"],
                          "low": data[json_table][primary_key[1]]["3. low"],
                          "close": data[json_table][primary_key[1]]["4. close"],
                          "volume": data[json_table][primary_key[1]]["5. volume"]}

        return self.__parse_to_db__(database, db_table, primary_key, processed_data)

    def parse_from_daily_time_series(self, database, primary_key):
        return self.__parse_from_db__(database, "DailyTimeSeries", primary_key, "date")


#r = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo")
#data = r.json()

#JSONParser = ParserJSON()
#parsedJSON = JSONParser.parse_from_json(data)

#db_manager = DatabaseManager("financial_db_test.db")

#DBParser = ParserDB()
#DBParser.parse_into_daily_time_series(db_manager, (51143, list(parsedJSON["Time Series (Daily)"])[1]), parsedJSON)
#print(DBParser.parse_from_daily_time_series(db_manager, (51143, "2023-12-05")))
