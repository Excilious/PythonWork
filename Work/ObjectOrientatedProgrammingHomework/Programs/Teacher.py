#Imports 
from Programs.Person import Person

"""
    Teacher - A SubClass that would inherit the data from the base
    class "Person". This would also use the super() method to gather attributes from the base
    class "Person".
"""

class Teacher(Person):
    List_Teachers = []

    #Constructor
    def __init__(self,Name:str,Age:int,Salary:float,Subjects_Taught,Gender:str="O"):
        #Inherits all attributes from base class
        super().__init__(Name,Age,Gender) 
        self.Salary = Salary
        self.Subjects_Taught = Subjects_Taught
        Teacher.List_Teachers.append(self)

    def __repr__(self):
        #__repr__: a function for which would be used to list out all the attributes in the class
        #In this case, __repr__ would be used to print out the attributes and how many teachers there are.
        self.NumberOfTeachers = len(Teacher.List_Teachers)
        print(f'\nName: {self.Name}\nAge: {self.Age}\nGender: {self.Gender}\nSalary: {self.Salary}\nSubjects Taught: {self.Subjects_Taught}\n\nThere Are A Total Of {self.NumberOfTeachers} Teacher(s).')