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
            for row in content:
                for value in row:
                    try:
                        numeric_value = int(value) if float(value).is_integer() else float(value)
                        num_values.append(numeric_value)
                    except ValueError:
                        pass
            if num_values:
                return sum(num_values) / len(num_values)
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
                return sum(num_values) / len(num_values)
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
                    return sum(num_values) / len(num_values)
                else:
                    raise ValueError("No values found in the file")