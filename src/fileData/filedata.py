
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
    def __init__(self, name, type,state):
        self.name = name
        self.type = type
        self.state = state
    
    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_state(self):
        return self.state

    def set_state(self, satate):
        self.state = satate

    def __str__(self) -> str:
        return str(self.name)    

class FileData():
    def __init__(self, datas):
        self.set_datas(datas)
        self.set_columns() 
    
    def get_datas(self):
        return(self.datas)
    
    def  set_datas(self, datas):
        self.datas = datas
    
    def get_columns(self) -> Columns:
        return self.columns

    def get_columns_name(self):
        return [c.name for c in self.columns]
    
    def set_columns(self):
        columns: List[Columns] = []
        if self.datas is not None and isinstance(self.datas, list):
            if len(self.datas):
                first_data = self.datas[0]
                if isinstance(first_data, (dict)):
                    for key, value in first_data.items():
                        columns.append(Columns(name=key, type=type(value).__name__, state=''))
        self.columns = columns
