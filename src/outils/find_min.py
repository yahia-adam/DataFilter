"""
Authors : Charbel Salhab, Theo Eloy, Adam Yahia Abdchafee
DataFilter Project
Fevrier 2024
"""


def find_min(content):
    if isinstance(content, list):
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