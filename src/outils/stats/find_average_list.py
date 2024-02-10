"""
Authors : Charbel Salhab, Theo Eloy, Adam Yahia Abdchafee
DataFilter Project
Fevrier 2024
"""


# find_average_list function used to find the average number of numeric list fields in csv, json, xml and yaml files and returns
# average value
def find_average_list(content):
    average_values = []
    # if content is a list
    if isinstance(content, list):
        # if content[0] is a list -> so it's a csv file
        if content and isinstance(content[0], list):
            field_name = None
            for row in content:
                numbers = []
                for idx, item in enumerate(row):
                    if ',' in item:
                        nbs = [int(num) for num in item.strip('\'').split(',')]
                        numbers.extend(nbs)
                        average_numbers = sum(numbers) / len(numbers)
                        average_values.append(average_numbers)
                        field_name = content[0][idx]
        # if content[0] is a dictionary -> so it's a json file
        elif content and isinstance(content[0], dict):
            field_name = None
            for item in content:
                numbers = []
                for key, value in item.items():
                    if isinstance(value, list):
                        numbers.extend(value)
                        average_numbers = sum(numbers) / len(numbers)
                        average_values.append(average_numbers)
                        field_name = key
    # if content is a dictionary (for yaml file)
    elif content and isinstance(content, dict):
        fields = []
        field_name = None
        for key, value in content.items():
            if isinstance(value, list):
                fields.extend(value)

        if fields:
            for item in fields:
                numbers = []
                for key, value in item.items():
                    if isinstance(value, list):
                        numbers.extend(value)
                        average_numbers = sum(numbers) / len(numbers)
                        average_values.append(average_numbers)
                        field_name = key
        else:
            raise ValueError("No values found in the file")
    else:
       raise ValueError("File not supported")

    average_values = [round(nb, 2) for nb in average_values]
    return field_name, average_values