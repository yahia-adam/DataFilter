from outils import upload_file

if __name__ == "__main__":
    datas = upload_file.upload_file("C:\\Users\\csalhab\\OneDrive\\Online Sessions\\3iabd1\\Scripting "
             "Python\\DataFilter\\datas\\inputs\\xml\\students.xml")
    if not datas:
        exit()
    else:
        print(datas)

        # pour acceder au valeur du json
        # print(datas['students'][0]['firstname'])

        # pour acceder au valeur de chaque etudiant
        # for student in datas.findall('student'):
        #     firstname = student.find('firstname').text
        #     lastname = student.find('lastname').text
        #     age = student.find('age').text
        #     apprentice = student.find('apprentice').text
        #     grades = [grade.text for grade in student.find('grades').iter('grade')]
        #
        #     print("Firstname:", firstname)
        #     print("Lastname:", lastname)
        #     print("Age:", age)
        #     print("Apprentice:", apprentice)
        #     print("Grades:", grades)
        #     print()