"""
Authors : Charbel Salhab, Theo Eloy, Adam Yahia Abdchafee
DataFilter Project
Fevrier 2024
"""


# find_average function used to find the average number of numeric fields in csv, json, xml and yaml files and
# returns average value
def find_average(content):
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
                return field_name, sum(num_values) / len(num_values)
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
                return field_name, sum(num_values) / len(num_values)
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
                    return field_name, sum(num_values) / len(num_values)
                else:
                    raise ValueError("No values found in the file")

    # if content is ET.element (for xml files only)
    elif isinstance(content, ET.Element):
        num_values = []
        for child in content.iter():
            try:
                value = int(child.text)
                num_values.append(value)
            except ValueError:
                pass

        if num_values:
            return sum(num_values) / len(num_values)
        else:
            raise ValueError("No values found in the file")
