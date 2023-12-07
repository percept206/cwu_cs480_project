import re

import requests

from parser import BaseParser
import json


class ParserJSON(BaseParser):
    def __init__(self):
        pass

    def parse(self, data):
        pass


    def parse_from_json(self, json_data):
        """
        Parses a JSON file, converting it into a dictionary. Additionally, replace all 'None' and "None" types with zero
            and convert stringified numbers into actual numeric types.

        Parameters:
            json_data (object): JSON data to be parsed, particularly from a request-libs request.
        Returns:
            dictionary: A dictionary containing JSON data
        """

        def replace_none_with_zero(data):
            if isinstance(data, dict):
                return {k: replace_none_with_zero(v) for k, v in data.items()}
            elif isinstance(data, list):
                return [replace_none_with_zero(item) for item in data]
            elif data is None or data == "None":
                return 0
            else:
                return data

        def convert_string_numbers(data):
            number_pattern = r"-?\d+(\.\d+)?"

            if isinstance(data, dict):
                return {k: convert_string_numbers(v) for k, v in data.items()}
            elif isinstance(data, list):
                return [convert_string_numbers(item) for item in data]
            elif isinstance(data, str):
                if re.fullmatch(number_pattern, data):
                    try:
                        return int(data)
                    except ValueError:
                        return float(data)
                return data
            else:
                return data

        resultA = replace_none_with_zero(json_data)
        resultB = convert_string_numbers(resultA)
        #print(resultB)
        return resultB

        pass


    def parse_to_json(self, data):

        pass


r = requests.get("https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=demo")
data = r.json()

JSONParser = ParserJSON()
JSONParser.parse_from_json(data)
