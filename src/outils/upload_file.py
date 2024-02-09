"""
Authors : Charbel Salhab, Theo Eloy, Adam Yahia Abdchafee
DataFilter Project
Fevrier 2024
"""

import csv, json, yaml
import xml.etree.ElementTree as ET


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
        return file_content

    # returns a dictionary containing all the yaml content
    elif file.endswith('.yaml'):
        with open(file, 'r') as f:
            # parse the yaml file and produce the corresponding python object
            # in this case a dictionary
            file_content = yaml.safe_load(f)
        return file_content

    # A checker :
    # https://docs.python.org/3/library/xml.etree.elementtree.html
    elif file.endswith('.xml'):
        t = ET.parse(file)
        r = t.getroot()
        return r

    # raise value error if file format is not supported
    else:
        raise ValueError("File Format Not Supported".format(file))