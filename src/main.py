from outils import read_file

if __name__ == "__main__":
    datas = read_file.read_file("/home/adam/Documents/esgi/DataFilter/datas/inputs/json/students.json")
    if (not datas):
        exit()
    for data in datas:
        print(data)