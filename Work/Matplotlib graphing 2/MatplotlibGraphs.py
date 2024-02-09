import asyncio
import json
import aiohttp
import matplotlib.pyplot as plot
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
from understat import Understat

from tkinter import *

#Async - appears to be a coroutine function that would run lines whilst awaiting?

plot.style.use('Style.mplstyle')# Applying house styles using a file.
 
LeagueTable = []
TeamTable = []
IsCreated = False

#---Fetching Data---#
async def PlayersOfSameTeam(Team):
    async with aiohttp.ClientSession() as ClientSession:
        NewUnderstat = Understat(ClientSession)
        Results = await NewUnderstat.get_team_players(
            Team,
            2022
        )
        return json.dumps(Results)
    
async def GetAllLeagues():
    async with aiohttp.ClientSession() as NewerClientSesion:
        NewestUnderstat = Understat(NewerClientSesion)
        MoreNewerResults = await NewestUnderstat.get_stats()
        return json.dumps(MoreNewerResults)
    
async def GetAllTeams(League):
    async with aiohttp.ClientSession() as NewClientSession:
        NewerUnderstat = Understat(NewClientSession)
        NewResults = await NewerUnderstat.get_teams(
            League,
            2023
        )
        return json.dumps(NewResults)
    
def FormatTable(Data):
    NewData = []
    for Contents in Data:
        if ("title" in Contents and not Contents['title'] in NewData):
            NewData.append(Contents['title'])
        elif ("league" in Contents and not Contents['league'] in NewData):
            NewData.append(Contents['league'])

    return NewData
    
def FetchingData(Frame,PlayerResultsDictionary):
    #--Plotting Said Data---#
    Names,Goals,ExpectedGoals = [],[],[]

    for x in range(len(PlayerResultsDictionary)):
        Names.append(PlayerResultsDictionary[x]['player_name'])
        Goals.append(float(PlayerResultsDictionary[x]['npg']))
        ExpectedGoals.append(float(PlayerResultsDictionary[x]['npxG']))

    GeneratePlot(Frame,Goals,ExpectedGoals)

def FinalGeneration(Values,Frame):
    PlayerResults = asyncio.run(PlayersOfSameTeam(Values))
    PlayerResultsDictionary = json.loads(PlayerResults)
    FetchingData(Frame,PlayerResultsDictionary)

def GenerateAllTeams(NewFrame,DefaultValues):
    GetTeamData = json.loads(asyncio.run(GetAllTeams(DefaultValues)))
    TeamTable = FormatTable(GetTeamData)

    TeamValues = StringVar(NewFrame)
    TeamValues.set("Select Your Team") 

    Options = OptionMenu(NewFrame, TeamValues,"DefaultValue", *TeamTable)
    Options.place(x=120,y=60)

    Enter = Button(NewFrame,text="Generate Graph!",width=15,command=lambda: FinalGeneration(TeamValues.get(),NewFrame),relief="groove")
    Enter.place(x=4,y=63)

def GeneratePlot(Frame,Goals,ExpectedGoals):
    NewFigure = Figure(figsize=(2.85,2.85),dpi=100)
    NewPlot = NewFigure.add_subplot(Goals,ExpectedGoals)
    NewPlot.plot([1**2 for i in range(101)])
    Canvas = FigureCanvasTkAgg(NewFigure, master=Frame)
    Canvas.draw()

    Canvas.get_tk_widget().place(x=55,y=100)

def CreateChoiceDialog():
    GetData = json.loads(asyncio.run(GetAllLeagues()))
    LeagueTable = FormatTable(GetData)

    NewFrame = Tk()
    NewFrame.geometry("400x400")
    NewFrame.maxsize(400,400)
    NewFrame.minsize(400,400)

    Title = Label(NewFrame,text="Team Picker",width=57,borderwidth=2,relief="groove")
    Title.place(x=0,y=0)

    DefaultValues = StringVar(NewFrame)
    DefaultValues.set("Select Your League") 

    Options = OptionMenu(NewFrame, DefaultValues,"DefaultOption", *LeagueTable)
    Options.place(x=120,y=29)

    Enter = Button(NewFrame,text="Choose League",relief="groove",width=15,command=lambda: GenerateAllTeams(NewFrame,DefaultValues.get()))
    Enter.place(x=4,y=32)

    NewFrame.mainloop()


CreateChoiceDialog()
    

