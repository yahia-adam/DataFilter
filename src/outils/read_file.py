import os
import json
import csv
import xml.etree.ElementTree as ET
import yaml

def get_filetype(file_path: str) -> str:
    return file_path.split('.')[-1]

def file_exist(file_path):
    return os.path.isfile(file_path)

def read_file(file_path):
    supported_filetype = ["json", "csv"]
    file_type = get_filetype(file_path)

    if (not file_exist(file_path)):
        print("Invalid file path!")
        return None
    if (file_type not in supported_filetype):
        print("Unsupported file!")
        return None
    else:
        try:
            if file_type == "json":
                with open(file_path, 'r') as file:
                    return json.load(file)
            elif file_type == "csv":
                with open(file_path, newline='') as file:
                    reader = csv.reader(file)
                    return list(reader)
            elif file_type == "xml":
                tree = ET.parse(file_path)
                root = tree.getroot()
                return root
            elif file_type == "yaml":
                with open(file_path, 'r') as file:
                    return yaml.safe_load(file)
        except Exception as e:
            print(f"Error reading file: {e}")
            return None