"""
Authors : Charbel Salhab, Theo Eloy, Adam Yahia Abdchafee
DataFilter Project
Fevrier 2024
"""


# find_max_list function used to find the max number of numeric list fields in csv, json, xml and yaml files and returns
# max value
def find_max_list(content):
    # if content is a list
    if isinstance(content, list):
        # if content[0] is a list -> so it's a csv file
        if content and isinstance(content[0], list):
            numbers = []
            field_name = None
            for row in content:
                for idx, item in enumerate(row):
                    if ',' in item:
                        nbs = [int(num) for num in item.strip('\'').split(',')]
                        numbers.extend(nbs)
                        field_name = content[0][idx]
            if numbers:
                return field_name, max(numbers)
            else:
                raise ValueError("No values found in the file")
        # if content[0] is a dictionary -> so it's a json file
        elif content and isinstance(content[0], dict):
            numbers = []
            field_name = None
            for item in content:
                for key, value in item.items():
                    if isinstance(value, list):
                        numbers.extend(value)
                        field_name = key

            if numbers:
                return field_name, max(numbers)
            else:
                raise ValueError("No values found in the file")
    # if content is a dictionary (for yaml file)
    elif content and isinstance(content, dict):
        fields = []
        field_name = None
        for key, value in content.items():
            if isinstance(value, list):
                fields.extend(value)

        if fields:
            numbers = []
            for item in fields:
                for key, value in item.items():
                    if isinstance(value, list):
                        numbers.extend(value)
                        field_name = key
            if numbers:
                return field_name, max(numbers)
            else:
                raise ValueError("No values found in the file")
        else:
            raise ValueError("No values found in the file")
