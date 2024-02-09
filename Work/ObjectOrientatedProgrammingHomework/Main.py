"""
Object Orientated Programming Work
    ¬ Abstraction - A menu system that would work by grabbing users inputs. This would be the main file that would be run on.
    ¬ Improvements - Seperating choice into functions

Tasks
    1). Add a teacher (to a list of teacher objects) [DONE]
    2). Add a 6th form Student (to a list of student objects) [DONE]
    3). List all the teachers (with a count of how many - class variable) [DONE]
    4). List all the 6th form students (with a count of how many class variable) [DONE]
    5). Search for a subject : print all teachers who teach it and all 6th form students taking it [DONE]
    6). Delete a teacher (drop from the list youll also need to amend option 3) [DONE]
    7). Delete a 6th form student (drop from the list youll also need to amend option 4) [DONE]
    8). Save all current teachers to an external binary file (use pickle example) [DONE]
    9). Save all current students teachers to an external binary file (use pickle example) [DONE]
    10). When the Program Starts, load all teachers and students (from their binary files) and set the Class variables (object 
    counts) to their correct values [DONE]
    11). Add other Sub Classes of Person for additional adults who may work at the school (your choice)  Add the relevant 
    functionality for these new people: (1-10 above  you decide) [DONE]
    12). Extend the Student Class so it also copes with Year Group, Tutor Group and Behaviour (Good, Average, Bad)  Add 
    the relevant functionality for these new attributes (1-10 above you decide) [DONE]
"""

"""
Marks
    1). File naming conventions
    2). Comments
    3). Docstrings
"""

#---Imports---#
from sys import path
import pickle
import sys

#---Program Imports---#
path.append("Programs")
from Programs import *

#Implemented a class system as more components from the menu would be organised
class Menu_System:

    #@Constructor
    def __init__(self):
        self.Get_From_Pickle()
        self.Menu()


    def Save_As_Pickle(self,Type):
        #Save_As_Pickle - Saves the class variable to a .bin file to be read from later on.
        #Current classes to load include: Teacher, Student and Principle

        Success = None
        try:
            #Attempting to save the file.
            #!BugError - Cannot save towards file: File may not exist or the directory would be incorrect.
            if (Type == "Teacher"):
                with open('TeacherDataStorage_Pickle.bin','wb') as Data:
                    pickle.dump(Teacher.List_Teachers,Data)
            elif (Type == "Student"):
                with open('StudentDataStorage_Pickle.bin','wb') as Data:
                    pickle.dump(Sixth_Form_Student.List_Students,Data)
            elif (Type == "Principle"):
                with open('PrincipleDataStorage_Pickle.bin','wb') as Data:
                    pickle.dump(Principle.PrincipleList,Data)
            Success = True
        except Exception as Err:
            print(f'Failed to save file. Reason: {Err}')
            Success = False

        if (Success):
            print("Successfully saved to .bin file.")

        input()
        self.Menu()


    def Get_From_Pickle(self):
        #Get_From_Pickle - Would attempt to load the data previously saved in the .bin file. Error 
        #would be printed out if there is no such directory found.

        #Current classes to load include: Teacher, Student and Principle
        Success = None
        try:
            with open('TeacherDataStorage_Pickle.bin','rb') as Teacher_Data_File:
                Teacher_Data = pickle.load(Teacher_Data_File)
            with open('StudentDataStorage_Pickle.bin','rb') as Student_Data_File:
                Student_Data = pickle.load(Student_Data_File)
            with open('PrincipleDataStorage_Pickle.bin','rb') as Principle_Data_File:
                Principle_Data = pickle.load(Principle_Data_File)

            #Restoring data within a class table. This table would be an object
            Teacher.List_Teachers = Teacher_Data
            Sixth_Form_Student.List_Students = Student_Data
            Principle.PrincipleList = Principle_Data
            Success = True
        except Exception as Err:
            print(f"Unable To Load Data. Reason: {Err}")
            Success = False

        if (Success):
            print("Successfully loaded data from files.")

        input()
        self.Menu()

    def Subject_Input(self,Type):
        #Subject_Input - A condition controlled loop that would be ran until the user has
        #entered the input 'End'.

        Flag_Closed = False
        Subjects_List = []

        while (not Flag_Closed):
            print(f'{Type} (Enter "End" When Done Inputting {Type}s.):')
            NewInput = str(input())
            if (NewInput == "End"):
                Flag_Closed = True
            else:
                #Appends to list if keyword 'End' would not be used.
                Subjects_List.append(NewInput)
        return Subjects_List
    
    
    def Menu(self):
        #Menu - A function that would control the users input.
        print("""
        [1]: Add A Teacher
        [2]: Add A Sixth Form Student
        [3]: Search For A Subject
        [4]: Removing A Teacher
        [5]: Removing A Student
        [6]: Save Current List Teacher To Pickle File (.bin)
        [7]: Save Current List Student To Pickle File (.bin)
              
        [Extention]:
        [8]: Add A Principle
        [9]: Removing A Principle 
        [10]: Save Current List Principle To Pickle File (.bin)
        [11]: Exit Program
            """)
        
        Choice = input("Choice: ")
        if (Choice.isdigit()):
            Choice = int(Choice)
        
        #Task 1 - Adding a teacher. Prints out required inputs and grabs and redirects the input back to the class.

        if (Choice == 1):
            Attributes = ["Name","Age","Salary","Subjects Taught","Gender"]
            Inputs = []

            #Indexes through the list and checks if the specific item 'Subjects Taught' would be found.
            for Type in Attributes:
                if (Type == "Subjects Taught"):
                    Inputs.append(self.Subject_Input("Subject"))
                else:
                    Choice = input(f'{Type}:')
                    Inputs.append(Choice)

            NewTeacher = Teacher(Inputs[0],Inputs[1],Inputs[2],Inputs[3],Inputs[4])
            NewTeacher.__repr__()

            input()
            self.Menu()

        #Task 2 - Adding a student. Similar to Task 1 where the input would be printed out then grabbed and redirected. 

        elif (Choice == 2):
            Attributes = ["Name","Age","School Name","Subjects Learning","Year Group","Tutor Group","Behaviour","Gender"]
            Inputs = []

            for Type in Attributes:
                if (Type == "Subjects Learning"):
                    Inputs.append(self.Subject_Input("Subject"))
                else:
                    Choice = input(f'{Type}:')
                    Inputs.append(Choice)

            NewStudent = Sixth_Form_Student(Inputs[0],Inputs[1],Inputs[2],Inputs[3],Inputs[4],Inputs[5],Inputs[6],Inputs[7])
            NewStudent.__repr__()

            input()
            self.Menu()

        #Task 3 - Searching for a subject. This would index through the class variable for which would check if 
        #the subject would be found within the class variable.

        elif (Choice == 3):
            People_In_Subjects = {}
            Subject_Input = str(input("What Subject Would You Like To Search For?: "))

            for ClassValue in Teacher.List_Teachers:
                for Subject in ClassValue.Subjects_Taught:
                    if (Subject == Subject_Input):
                        People_In_Subjects[ClassValue.Name] = "Teacher" 
   
            for ClassValue in Sixth_Form_Student.List_Students:
                for Subject in ClassValue.List_Of_Subjects:
                    if (Subject == Subject_Input):
                        People_In_Subjects[ClassValue.Name] = "Student"

            for ClassValue in Principle.PrincipleList:
                for Subject in ClassValue.WorkNeededToDo:
                    if (Subject == Subject_Input):
                        People_In_Subjects[ClassValue.Name] = "Principle"

            if (len(People_In_Subjects) >= 1):
                for Names in People_In_Subjects.keys():
                    print(f'[{People_In_Subjects[Names]}] {Names} - {Subject_Input}')
            else:
                print(f'Unable to find anyone who has {Subject_Input}.')

            input()
            self.Menu()

        #Task 4 - Deleting a teacher from the system. Checks the name of the teacher to remove. This would be indexed
        #with enuemrate. The value would be used to remove the data from the table.

        elif (Choice == 4):
            Success = False
            People_To_Remove = str(input("What Teacher Would You Like To Remove?: "))

            for Index,ClassValue in enumerate(Teacher.List_Teachers):
                if (ClassValue.Name == People_To_Remove):
                    Success = True
                    Teacher.List_Teachers.remove(Teacher.List_Teachers[Index])

            if (Success): 
                print(f'{People_To_Remove} Has Been Removed From Teachers.')
            else:
                print(f'Cannot find {People_To_Remove}.')

            input()
            self.Menu()

        #Task 5 - Deleating a student from the system. This would be similar to Task 4
        elif (Choice == 5):
            Success = False
            People_To_Remove = str(input("What Teacher Would You Like To Remove?: "))

            for Index,ClassValue in enumerate(Student.List_Students):
                if (ClassValue.Name == People_To_Remove):
                    Success = True
                    Sixth_Form_Student.List_Students.remove(Sixth_Form_Student.List_Students[Index])

            if (Success):
                print(f'{People_To_Remove} Has Been Removed From Sixth Form Students.')
            else:
                print(f'Cannot find {People_To_Remove}')

            input()
            self.Menu()

        #Task 6 - Save current list of teachers into a bin file (pickle). Redirects to above function
        elif (Choice == 6):
            self.Save_As_Pickle("Teacher")

        #Task 7 - Save current list of student into a bin file (pickle). Redirects to above function.
        elif (Choice == 7):
            self.Save_As_Pickle("Student")

        #-------Extention--------#


        #Task 12 - Creating a new subclass [Adding a principle]
        elif (Choice == 8):
            Attributes = ["Name","Age","Work Needed To Do","School Funding","Salary","Gender"]
            Inputs = []

            for Type in Attributes:
                if (Type == "Work Needed To Do"):
                    Inputs.append(self.Subject_Input("Work Needed To Do"))
                else:
                    Choice = input(f'{Type}:')
                    Inputs.append(Choice)

            NewStudent = Principle(Inputs[0],Inputs[1],Inputs[2],Inputs[3],Inputs[4],Inputs[5])
            NewStudent.__repr__()

            input()
            self.Menu()

        #Task 12 - Creating a new subclass [Deleating a principle]
        elif (Choice == 9):
            Success = False
            People_To_Remove = str(input("What Principle Would You Like To Remove?: "))

            for Index,ClassValue in enumerate(Principle.PrincipleList):
                if (ClassValue.Name == People_To_Remove):
                    Success = True
                    Principle.PrincipleList.remove(Principle.PrincipleList[Index])

            if (Success):
                print(f'{People_To_Remove} Has Been Removed From Principle.')
            else:
                print(f'Cannot find {People_To_Remove}')

            input()
            self.Menu()

        #Task 12 - Saving principle list to pickle
        elif (Choice == 10):
            self.Save_As_Pickle("Principle")

        #When exiting the program, returns to normal command line and closes the program
        elif (Choice == 11):
            print("Exiting program...")
            sys.exit()
        
        #No inputs match the conditioned input. Print message and redirects to main menu.
        else:
            input("Invalid input! Press any key to continue.")
            self.Menu()


if (__name__ == '__main__'):
    NewMenu = Menu_System()