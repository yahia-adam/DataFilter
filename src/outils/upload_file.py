"""
Authors : Charbel Salhab, Theo Eloy, Adam Yahia Abdchafee
DataFilter Project
Fevrier 2024
"""

import csv, json


# upload_file function used to upload csv, json, xml and yaml files and returns its content
def upload_file(file):
    # returns a list of lists representing each line of the csv file
    if file.endswith('.csv'):
        file_content = []
        with open(file, 'r') as f:
            reader = csv.reader(f)
            for line in reader:
                file_content.append(line)
        # print(file_content) test done in main.py
        return file_content

    # returns a dictionary containing all the json content
    elif file.endswith('.json'):
        with open(file, 'r') as f:
            file_content = json.load(f)
            # return file_content
        return file_content
