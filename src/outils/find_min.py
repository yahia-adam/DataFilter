"""
Authors : Charbel Salhab, Theo Eloy, Adam Yahia Abdchafee
DataFilter Project
Fevrier 2024
"""


def find_min(content):
    if isinstance(content, list):
        num_values = [int(value) for row in content for value in row if value.replace('.', '', 1).isdigit()]
        return min(num_values)
