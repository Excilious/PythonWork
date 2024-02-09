"""
    Person - A baseclass in which may be inherited by other subclasses. This class
    would have such attributes such as Name, Age and Gender. This would be used as a creator
    of other classses by adding attributes.
"""

class Person:
    #Constructor - Would be called as soon as the main class would be called
    def __init__(self,Name:str,Age:int,Gender:str="O"):
        self.Name = Name
        self.Age = Age
        self.Gender = Gender

    #__repr__ a reporting function for which formats the attributes as shown below when the class object would be printed out
    def __repr__(self):
        print(f'Name: {self.Name}\nAge: {self.Age}\nGender: {self.Gender}')