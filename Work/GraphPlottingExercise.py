#Imports
import asyncio
import json
import aiohttp
import matplotlib.pyplot as plot
from understat import Understat

#Other Imports
import numpy
import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

Names = []
Goals = []
ExpectedGoals = []

#Gathering data
async def GetTeam():
    async with aiohttp.ClientSession() as Session:
        NewUnderstat = Understat(Session)
        Results = await NewUnderstat.get_teams(
            "EPL",
            2023
        )
        return json.dumps(Results)

async def GetPlayersOfSameTeam():
     async with aiohttp.ClientSession() as Session:
        NewUnderstat = Understat(Session)
        Results = await NewUnderstat.get_player_of_teams(
            "Nottingham Forest",
            2023
         )
        return json.dumps(Results)
    
def GatherUserInput():
    TextInput = simpledialog.askstring("Teams","Enter the team you want.")
    if (TextInput == None or TextInput == ""):
        messagebox.ERROR("Teams","Invalid option!")
        GatherUserInput()
    return TextInput

def CreateTeamGUI():
    UI = tkinter.Tk()
    UI.title('Dude')
    UI.geometry("500x500")

    TreeColumns = ('Dude')
    TreeInstance = ttk.Treeview(UI, columns=TreeColumns, show='headings')

    TreeInstance.heading('Dude',text='Dude')
    NewData = GetTeam()

    for Data in NewData:
        print(Data)
        #TreeInstance.insert('',tkinter.END,values=Data)

    #TODO - Add a binder
    TreeInstance.grid(row=0,column=0, sticky='nsew')

    ScrollbarInstance = ttk.Scrollbar(UI, orient=tkinter.VERTICAL,command=TreeInstance.yview)
    TreeInstance.configure(yscroll=ScrollbarInstance.set)
    ScrollbarInstance.grid(row=0,column=1,sticky='ns')

    UI.mainloop()
    
    
        
def GetGraphData():
    PlayerData = asyncio.run(GetPlayersOfSameTeam())
    PlayerDataDict = json.loads(PlayerData)

    for Index in range(len(PlayerDataDict)):
        Names.append(PlayerDataDict[Index]['player_name'])
        Goals.append(float(PlayerDataDict[Index]['npg']))
        ExpectedGoals.append(float(PlayerDataDict[Index]['npxG']))

    PlotGraphFromData()

def PlotGraphFromData():
    Figure, Axis = plot.subplots()
    Axis.scatter(Goals, ExpectedGoals)

    for Counter in range(0,5):
        plot.text(Goals[Counter], ExpectedGoals[Counter], Names[Counter])
            
    Axis.set_xlabel('Goals')
    Axis.set_ylabel('Expected Goals')
    Axis.set_facecolor('grey')
    Axis.xaxis.label.set_color('red')

    plot.show()

if (__name__ == '__main__'):
    PlayerData = asyncio.run(GetTeam())
    PlayerDataDict = json.loads(PlayerData)

    CreateTeamGUI()
        
    
    