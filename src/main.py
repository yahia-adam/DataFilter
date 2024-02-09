from outils import upload_file

if __name__ == "__main__":
    datas = upload_file.upload_file("C:\\Users\\csalhab\\OneDrive\\Online Sessions\\3iabd1\\Scripting "
             "Python\\DataFilter\\datas\\inputs\\yaml\\students.yaml")
    if not datas:
        exit()
    else:
        print(datas['students'][0]['firstname'])