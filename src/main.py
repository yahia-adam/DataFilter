from outils import upload_file

if __name__ == "__main__":
    datas = upload_file.upload_file("C:\\Users\\csalhab\\OneDrive\\Online Sessions\\3iabd1\\Scripting "
             "Python\\DataFilter\\datas\\inputs\\csv\\students.csv")
    if not datas:
        exit()
    for data in datas:
        print(data)