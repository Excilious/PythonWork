#Imports
from Programs.Student import Student
from random import randint

"""
    Sixth_Form_Student - A SubSub class in which would inherit the values from "Student" for which
    would inherit the values from the "Person" class. This would also use the super() method to get attributes
    from the "Student" class for which have gotten attributes from the "Person" class
"""

class Sixth_Form_Student(Student):
    List_Students = []
    BehaviourTypes = ["Good","Average","Bad"]
    #Constructor

    def __init__(self,Name:str,Age:int,School_Name:str,List_Of_Subjects:object,YearGroup:int,TutorGroup:str,Behavior:str="Average",Gender:str="O"):
        #We could hand over the error checking to the Students class but its better to check from the source.
        if (Behavior not in Sixth_Form_Student.BehaviourTypes):
            Behavior = Sixth_Form_Student[randint(0,len(Sixth_Form_Student.BehaviourTypes)-1)]

        #Inherits all attributes from the "Student" class
        super().__init__(Name,Age,School_Name,Behavior,YearGroup,TutorGroup,Gender)
        self.List_Of_Subjects = List_Of_Subjects
        Sixth_Form_Student.List_Students.append(self)

    def __repr__(self):
        #__repr__: Once again this would be used to print out the attributes for this class.
        #This would do the same function as the Teacher __repr__()
        self.NumberOfStudents = len(Sixth_Form_Student.List_Students)
        print(f'\nName: {self.Name}\nAge: {self.Age}\nGender: {self.Gender}\nSchool Name: {self.Name_Of_School}\nSubjects Learning: {self.List_Of_Subjects}\n\nThere Are A Total Of {self.NumberOfStudents} Students(s).')
