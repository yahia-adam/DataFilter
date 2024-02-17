import tkinter as tk
from tkinter import ttk
import json

def load_json_data():
    # Charger vos données JSON
    json_data = '''
    [
        {
            "firstname": "John",
            "lastname": "Doe",
            "age": 22,
            "apprentice": true,
            "grades": {
                "math": 10,
                "histoire": 15,
                "grades": {
                    "math": 10,
                    "histoire": 15
                }
            }
        },
        {
            "firstname": "Jane",
            "lastname": "Smith",
            "age": 21,
            "apprentice": false,
            "grades": {
                "math": 10,
                "histoire": 15,
                "grades": {
                    "math": 10,
                    "histoire": 15
                }
            }
        }
    ]
    '''
    return json.loads(json_data)

def main():
    root = tk.Tk()
    root.title("JSON Viewer")

    json_data = load_json_data()

    columns = list(json_data[0].keys())
    tree = ttk.Treeview(root, columns=columns, show="headings")

    # Configurer les colonnes avec les noms de clés
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")

    # Insérer les données dans le tableau
    for item in json_data:
        values = [str(item[col]) for col in columns]
        tree.insert('', 'end', values=values)

    tree.pack(expand=True, fill=tk.BOTH)

    root.mainloop()

if __name__ == "__main__":
    main()
