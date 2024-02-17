"""
Authors : Charbel Salhab, Theo Eloy, Adam Yahia Abdchafee
DataFilter Project
Fevrier 2024
"""
import json
import csv
import yaml
import xml.etree.ElementTree as ET

def open_json(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error opening JSON file: {e}")
        return None

def open_csv(filepath):
    try:
        with open(filepath, 'r', newline='') as file:
            csv_reader = csv.DictReader(file)
            data = [row for row in csv_reader]
        return data
    except Exception as e:
        print(f"Error opening CSV file: {e}")
        return None

def open_yaml(filepath):
    try:
        with open(filepath, 'r') as file:
            data = yaml.safe_load(file)
        return data
    except Exception as e:
        print(f"Error opening YAML file: {e}")
        return None

def open_xml(filepath):
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
        data = []
        for item in root.findall('item'):
            item_data = {child.tag: child.text for child in item}
            data.append(item_data)
        return data
    except Exception as e:
        print(f"Error opening XML file: {e}")
        return None

def upload_file(filepath):
    allowed_file_types = ['json', 'csv', 'xml', 'yaml']
    filetype = filepath.split(".")[-1].lower()
    if filetype not in allowed_file_types:
        raise Exception(f'Only {", ".join(allowed_file_types)} files are accepted.')

    if filetype == "json":
        datas = open_json(filepath)
        return datas
    elif filetype == "csv":
        datas = open_csv(filepath)
        return datas
    elif filetype == "yaml":
        datas = open_yaml(filepath)
        return datas
    else:
        datas = open_xml(filepath)
        return datas
    return None

filepathjson='/home/adam/Documents/esgi/DataFilter/datas/inputs/json/students.json'
filepathcsv='/home/adam/Documents/esgi/DataFilter/datas/inputs/csv/students.csv'
filepathyaml='/home/adam/Documents/esgi/DataFilter/datas/inputs/yaml/students.yaml'
filepathxml='/home/adam/Documents/esgi/DataFilter/datas/inputs/xml/students.xml'

# print(upload_file(filepathxml))