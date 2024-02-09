"""
Authors : Charbel Salhab, Theo Eloy, Adam Yahia Abdchafee
DataFilter Project
Fevrier 2024
"""

import xml.etree.ElementTree as ET


# find_min function used to find the min number of numeric fields in csv, json, xml and yaml files and returns min value
def find_min(content):
    # if content is a list
    if isinstance(content, list):
        # if content[0] is a list -> so it's a csv file
        if content and isinstance(content[0], list):
            num_values = []
            for row in content:
                for value in row:
                    try:
                        numeric_value = int(value) if value.is_integer() else float(value)
                        num_values.append(numeric_value)
                    except ValueError:
                        pass
            if num_values:
                return min(num_values)
            else:
                raise ValueError("No values found in the file")
        # if content[0] is a dictionary -> so it's a json file
        elif content and isinstance(content[0], dict):
            num_values = []
            for item in content:
                for value in item.values():
                    if isinstance(value, (int, float)) and (value != True and value != False):
                        num_values.append(value)
            if num_values:
                return min(num_values)
            else:
                raise ValueError("No values found in the file")
    # if content is a dictionary (for yaml file)
    elif isinstance(content, dict):
        for key, value in content.items():
            if isinstance(value, list):
                num_values = []
                for item in value:
                    if isinstance(item, dict):
                        for k, v in item.items():
                            if isinstance(v, (int, float)) and (v != True and v != False):
                                num_values.append(v)
                if num_values:
                    return min(num_values)
                else:
                    raise ValueError("No values found in the file")
    # if content is ET.element (for xml files only)
    elif isinstance(content, ET.Element):
        num_values = []
        for child in content.iter():
            if child.text.replace('.', '', 1).isdigit():
                if '.' in child.text:
                    num_values.append(float(child.text))
                else:
                    num_values.append(int(child.text))
        if num_values:
            return min(num_values)
        else:
            raise ValueError("No values found in the file")
