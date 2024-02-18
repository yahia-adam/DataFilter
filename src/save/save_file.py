"""
Authors : Charbel Salhab, Theo Eloy, Adam Yahia Abdchafee
DataFilter Project
Fevrier 2024
"""

import json
import csv
import xml.etree.ElementTree as ET

def save_json(filepath, datas):
    try:
        with open(filepath, 'w') as file:
            json.dump(datas, file, indent=2)
        print(f"JSON data saved to {filepath}")
    except Exception as e:
        print(f"Error saving JSON data: {e}")

def save_csv(filepath, datas):
    try:
        with open(filepath, 'w', newline='') as file:
            csv_writer = csv.DictWriter(file, fieldnames=datas[0].keys())
            csv_writer.writeheader()
            csv_writer.writerows(datas)
        print(f"CSV data saved to {filepath}")
    except Exception as e:
        print(f"Error saving CSV data: {e}")


def save_yaml(filepath, datas):
    pass

def save_xml(filepath, datas):
    try:
        root = ET.Element("data")

        for data in datas:
            item = ET.SubElement(root, "item")
            for key, value in data.items():
                sub_element = ET.SubElement(item, key)
                sub_element.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filepath)
        
        print(f"XML data saved to {filepath}")
    except Exception as e:
        print(f"Error saving XML data: {e}")

def save_sa_file(filepath, datas):
    allowed_file_types = ['json', 'csv', 'xml', 'yaml']
    filetype = filepath.split(".")[-1].lower()
    if filetype not in allowed_file_types:
        raise Exception(f'Only {", ".join(allowed_file_types)} files are accepted.')

    if filetype == "json":
        datas = save_json(filepath, datas)
        return datas
    elif filetype == "csv":
        datas = save_csv(filepath, datas)
        return datas
    elif filetype == "yaml":
        datas = save_yaml(filepath, datas)
        return datas
    else:
        datas = save_xml(filepath, datas)
        return datas
    return None