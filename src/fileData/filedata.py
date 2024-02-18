
from typing import List
"""
    Entiers (int) :
        Minimum (min): 0
        Maximum (max): 10
        Moyenne (avg): 4

    Exemple : {"min": 0, "max": 10, "avg": 4}

    Chaînes de caractères (str) :
        Longueur minimale (len-min): 0
        Longueur maximale (len-max): 10
        Total des longueurs (total-len)

    Exemple : {"len-min": 0, "len-max": 10, "total-len": 200}

    Listes :
        Moyenne (mean): 10
        Écart type (std): ...
        Minimum (min): 0
        Maximum (max): 10

    Exemple : {"mean": 10, "std": ..., "min": 0, "max": 10}

"""

class Columns():
    def __init__(self, name, type, state):
        self.name = name
        self.type = type
        self.state = state
    
    @staticmethod
    def create_from_name(name, type, state):
        return Columns(name, type, state)

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def __str__(self) -> str:
        return str(self.name)

class FileData():
    def __init__(self, datas):
        self.columns, self.datas = FileData.flatten_dict(datas)

    def get_datas(self):
        return self.datas
    
    def set_datas(self, datas):
        self.datas = datas

    def get_columns(self):
        return self.columns

    def update_column_state(self, datas):
            column_data = [item[column_name] for item in datas]

    def get_columns_name(self):
        return [c.name for c in self.columns]
    
    @staticmethod
    def flatten_dict(dictionary, parent_key='', sep='_'):
        columns = []
        data = []

        for key, value in dictionary.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key

            if isinstance(value, dict):
                # Récursivement, traite les sous-dictionnaires
                sub_columns, sub_data = FileData.flatten_dict(value, new_key, sep=sep)
                columns.extend(sub_columns)
                data.extend(sub_data)
            elif isinstance(value, list):
                # Traite les listes en les convertissant en chaînes
                columns.append(Columns.create_from_name(new_key, 'list', ''))
                data.append(str(value))
            else:
                # Traite les valeurs simples
                columns.append(Columns.create_from_name(new_key, type(value).__name__, ''))
                data.append(value)

        return columns, data
