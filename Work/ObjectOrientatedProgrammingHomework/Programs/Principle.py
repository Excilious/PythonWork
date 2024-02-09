from Programs.Person import Person

"""
    Principle - A base class for which would inherit some attributes from the Person class. The Principle class
    would have some attributes to use for its own class.
"""

class Principle(Person):
    #A class variable for which would store the 'self' objects. This would contain 
    GenderList = ["M","F","O"]
    PrincipleList = []

    #@Constructor - creates new attributes for the new instance.
    def __init__(self,Name:str,Age:int,WorkNeededToDo:object,School_Funding:float,Salary:float,Gender:str="O"):
        super().__init__(Name,Age,Gender)
        self.WorkNeededToDo = WorkNeededToDo
        self.SchoolFunding = School_Funding
        self.Salary = Salary
        
        Principle.PrincipleList.append(self)

    #__repr__ - Reports the values of the class using this format.
    def __repr__(self):
        NumberOfPrinciples = len(Principle.PrincipleList)
        print(f'\nName: {self.Name}\nAge: {self.Age}\nGender: {self.Gender}\nSalary: {self.Salary}\nWork Needed To Do: {self.WorkNeededToDo}\nSchool Funding: {self.SchoolFunding}\n\nThere Are Currently {NumberOfPrinciples} Principle(s).')