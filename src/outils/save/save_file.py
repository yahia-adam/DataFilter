"""
Authors : Charbel Salhab, Theo Eloy, Adam Yahia Abdchafee
DataFilter Project
Fevrier 2024
"""

import shutil

# A checker
# https://docs.python.org/3/library/shutil.html


def save_file(source, destination):
    try:
        shutil.copy(source, destination)
    except Exception as e:
        print("Error while saving : ", str(e))

