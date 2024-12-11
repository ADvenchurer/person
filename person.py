import pygame

class students():
    
    school = ""
    name = ""
    age = 0
    grade = 0

    def __init__(self):
        print()
        

    def change_details(self):
        print("Enter your school: ")
        self.school = input()
        print("Enter the grade of your student: ")
        self.grade = input()
        print("Enter your age: ")
        self.age = int(input())
        print("Enter the name of the student")
        self.name = input()


    def show_details(self):
        print("The details of the student are:")
        print("Name: " + self.name)
        print(str(self.age) + " years old")
        print("In grade " + self.grade)
        print("In " + self.school)


Adam = students()
Adam.change_details()
Adam.show_details()

Shivani = students()
Shivani.change_details()
Shivani.show_details()



