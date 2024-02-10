"""
Authors : Charbel Salhab, Theo Eloy, Adam Yahia Abdchafee
DataFilter Project
Fevrier 2024
"""

import xml.etree.ElementTree as ET


# find_max function used to find the max number of numeric fields in csv, json, xml and yaml files and returns max value
def find_max(content):
    # if content is a list
    if isinstance(content, list):
        # if content[0] is a list -> so it's a csv file
        if content and isinstance(content[0], list):
            num_values = []
            field_name = None
            for row in content:
                for idx, value in enumerate(row):
                    try:
                        numeric_value = int(value) if float(value).is_integer() else float(value)
                        num_values.append(numeric_value)
                        if field_name is None:
                            field_name = content[0][idx]
                    except ValueError:
                        pass
            if num_values:
                return field_name, max(num_values)
            else:
                raise ValueError("No values found in the file")
        # if content[0] is a dictionary -> so it's a json file
        elif content and isinstance(content[0], dict):
            num_values = []
            field_name = None
            for item in content:
                for key, value in item.items():
                    if isinstance(value, (int, float)) and (value != True and value != False):
                        num_values.append(value)
                        if field_name is None:
                            field_name = key
            if num_values:
                return field_name, max(num_values)
            else:
                raise ValueError("No values found in the file")
    # if content is a dictionary (for yaml file)
    elif isinstance(content, dict):
        for key, value in content.items():
            if isinstance(value, list):
                num_values = []
                field_name = None
                for item in value:
                    if isinstance(item, dict):
                        for k, v in item.items():
                            if isinstance(v, (int, float)) and (v != True and v != False):
                                num_values.append(v)
                                if field_name is None:
                                    field_name = k
                if num_values:
                    return field_name, max(num_values)
                else:
                    raise ValueError("No values found in the file")
    # if content is ET.element (for xml files only)
    # elif isinstance(content, ET.Element):
        