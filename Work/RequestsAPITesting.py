#Testing the support library
import PythonSupportLibrary
SupportTable = {}
Table = {}

Table["Hi"] = "Hello"
NewTable = PythonSupportLibrary.table()
NewTable.insert(SupportTable,"Hi","Hello")

print(SupportTable)
print(Table)