from caseconverter import camelcase
import re
from dateutil.parser import isoparse

class schemaService():

    def get_schema(self, data):
        items = []
        # Identifying field types
        for key in data[0].keys():
            for value in data:
                # Checking to see if value is not null
                schemaValue = self.filter_dict(value, key)
                if schemaValue is True:
                    schemaItem = {
                        "display": key,
                        "name": self.to_camel_case(key),
                        "type": self.check_type(value[key]),
                        "options": self.check_options(value[key], data, key)
                    }
                    items.append(schemaItem)
                    break

        return items

    def filter_dict(self, dict, currentKey):
        if dict[currentKey] is not None:
            return True

    def check_type(self, value):
        itemType = type(value).__name__
        if itemType == "str":
            if self.is_date(value):
                itemType = "date"

        # Equivalent to switch case statement
        return {
            "int": "INTEGER",
            "float": "FLOAT",
            "str": "TEXT",
            "date": "DATE",
            "bool": "BOOLEAN",
            "list": "OPTION"
        }.get(itemType, "ANY")

    def is_date(self, string):
        try:
            isoparse(string)
            return True

        except ValueError:
            return False

    def check_options(self, value, data, key):
        itemType = self.check_type(value)
        if itemType == "OPTION":
            return self.filter_options(data, key)
        else:
            return []

    def to_camel_case(self, value):
        return camelcase(re.sub('[()]', '', value))

    # Checking all the possible options available and returning only unique items
    def filter_options(self, data, key):
        allOptions = []
        for values in data:
            for v in values[key]:
                if v not in allOptions:
                    allOptions.append(v)

        return allOptions