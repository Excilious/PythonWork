#Brings all the classes from the files as shown
#from {File.txt} import {Class}

#EDIT - It seems as if from {File} import {Class} would not be enough and instead you 
#would need to specifiy towards python the current directory in which the module would be in

"""
    __init__.py - A file for which python would attempt to load instantly. This would be executed during the first execution
    of the __main__ file.

    Abstraction - Would gather all classes from the directory of the folder.
"""

from Programs.Person import *
from Programs.Sixth_Form_Student import *
from Programs.Student import *
from Programs.Teacher import *
from Programs.Principle import *