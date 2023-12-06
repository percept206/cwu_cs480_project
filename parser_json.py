from cwu_cs480_project.parser import BaseParser
import json

class ParserJSON(BaseParser):
    def __init__(self):
        pass

    def parse(self, data):
        pass

    def parse_from_json(self, json_data):
        """
        Parses a JSON file, converting it into a dictionary.

        Parameters:
            json_data (object): JSON data to be parsed, particularly from a request-libs request.
        Returns:
            dictionary: A dictionary containing JSON data
        """
        pass

    def parse_to_json(self, data):
        pass