import asyncio
import json
import aiohttp
import matplotlib.pyplot as plot
from understat import Understat

from tkinter import *

#Async - appears to be a coroutine function that would run lines whilst awaiting?

plot.style.use('Style.mplstyle')# Applying house styles using a file.
 
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
    
def FetchingData(PlayerResultsDictionary):
    #--Plotting Said Data---#
    Names,Goals,ExpectedGoals = [],[],[]

    for x in range(len(PlayerResultsDictionary)):
        Names.append(PlayerResultsDictionary[x]['player_name'])
        Goals.append(float(PlayerResultsDictionary[x]['npg']))
        ExpectedGoals.append(float(PlayerResultsDictionary[x]['npxG']))

    plot.scatter(Goals, ExpectedGoals)

    for i in range(0,5):
        plot.text(Goals[i], ExpectedGoals[i], Names[i])

    plot.show()

def CreateChoiceDialog():
    NewFrame = Tk()
    NewFrame.geometry("400x150")
    NewFrame.maxsize(400,130)
    NewFrame.minsize(400,130)

    Title = Label(NewFrame,text="Team Picker",width=57,borderwidth=2,relief="groove")
    Title.place(x=0,y=0)

    DefaultValues = StringVar(NewFrame)
    DefaultValues.set("Select Your League") 

    Options = OptionMenu(NewFrame, DefaultValues, "one", "two", "three")
    Options.place(x=100,y=29)

    Enter = Button(NewFrame,text="Select League",relief="raised",width=11)
    Enter.place(x=5,y=32)

    DefaultValues = StringVar(NewFrame)
    DefaultValues.set("Select Your Team") 

    Options = OptionMenu(NewFrame, DefaultValues, "one", "two", "three")
    Options.place(x=90,y=60)

    Enter = Button(NewFrame,text="Select Team",width=10)
    Enter.place(x=5,y=62)

    Enter = Button(NewFrame,text="Generate Graph!",width=27)
    Enter.place(x=102,y=102)

    NewFrame.mainloop()

def MenuSystem():
    #Getting user leagues
    GetData = json.loads(asyncio.run(GetAllLeagues()))
    ListData = FormatTable(GetData)
    for Index,Contents in enumerate(ListData):
        print(f"[{Index}]: {Contents}")

    UserChoice = int(input("Enter Your League\n"))
    LeaguePicked = ListData[UserChoice]

    #Getting user teams
    GetTeamData = json.loads(asyncio.run(GetAllTeams(LeaguePicked)))
    ListTeamData = FormatTable(GetTeamData)
    for Index,Contents in enumerate(ListTeamData):
        print(f"[{Index}]: {Contents}")

    UserChoice = int(input("Enter Your Team\n"))
    TeamPicked = ListTeamData[UserChoice]

    PlayerResults = asyncio.run(PlayersOfSameTeam(TeamPicked))
    PlayerResultsDictionary = json.loads(PlayerResults)
    FetchingData(PlayerResultsDictionary)


MenuSystem()
    

