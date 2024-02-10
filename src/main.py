"""
Authors : Charbel Salhab, Theo Eloy, Adam Yahia Abdchafee
DataFilter Project
Fevrier 2024
"""

from outils.upload import upload_file
from outils.stats import find_average
from outils.stats import find_percentage

if __name__ == "__main__":
    datas = upload_file.upload_file("C:\\Users\\csalhab\\OneDrive\\Online Sessions\\3iabd1\\Scripting "
             "Python\\DataFilter\\datas\\inputs\\json\\students.json")
    if not datas:
        exit()
    else:
        x, y = find_average.find_average(datas)
        print(x, y)
        # print(datas)
        # a, x, y = find_percentage.find_percentage(datas)
        # print(a, x, "True", y, "False")

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

    # src = ("C:\\Users\\csalhab\\OneDrive\\Online Sessions\\3iabd1\\Scripting "
    #        "Python\\DataFilter\\datas\\inputs\\xml\\students.xml")
    # destination = input("test path to save in :")
    # save_file.save_file(src, destination)

