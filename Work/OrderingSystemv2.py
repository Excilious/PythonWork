#!nonstrict

from tkinter import * 
from tkinter import ttk 
from tkinter import font 

class Window: 
    OrderDatabase = {} 

    #Basic UI Events.
    #Parameter 'Event' would not be used.
    def OnButtonEvent(self,Event):   
        Event.widget.configure(fg=self.PrimaryColours["ForegroundActive"])
    
    def OnButtonExit(self,Event):
        Event.widget.configure(fg=self.PrimaryColours["ForegroundHiddenSharp"])

    def __init__(self): 
        #Starts up all current instances
        self.MasterWindow = Tk() 
        self.FrameConfigurationsBuilder() 
        self.BaseWindowBuilder()

    def FrameConfigurationsBuilder(self): 
        #Create the functions that we would need to use.
        #This can be configured anytime (Including themes and font).
        #Any values will globally affect the program
        self.FrameFunctions = {
            "OrderFrame": self.RenderCurrentOrderFrame,
            "CreateOrder":self.CreateOrderFrame
        }

        self.Resolution = [900,500]
        self.PrimaryColours = {
            "ForegroundHidden":'#f5f2f2',
            "ForegroundActive":'#03fc98',
            "ForegroundHiddenSharp":'#cccccc'
        }
        self.Options = ["New Order","Get Order","Sent Orders"]

        self.MasterWindow.geometry(str(self.Resolution[0])+"x"+str(self.Resolution[1])) 
        self.MasterWindow.maxsize(self.Resolution[0],self.Resolution[1]) 
        self.MasterWindow.minsize(self.Resolution[0],self.Resolution[1]) 

        self.FontLibrary = { 
            "Helvetica":font.Font(family="Helvetica",size=9),
            "Helvetica_Options":font.Font(family="Helvetica",size=9,weight="bold"),
            "Helvetica_Title":font.Font(family='Helvetica', size=12, weight='bold'), 
            "Helvetica_Title_Alternate":font.Font(family="Helvetica",size=11,weight="bold"),
            "Helvetica_Button": font.Font(family="Helvetica", size=9, weight="bold"),
            "Helvetica_Italic": font.Font(family="Helvetica",size=9,slant="italic")
        } 
        self.ActiveButtons = []

    def BaseWindowBuilder(self):
        #The current program would not need to be globalised. This would 
        #mean that the frames can be using the current variable. The only
        #variable would be Baseframe (The core frame to attach)
        self.BaseFrame = Frame(self.MasterWindow,width=self.Resolution[0],height=self.Resolution[1],bg=self.PrimaryColours["ForegroundHidden"])
        self.BaseFrame.place(x=0,y=0)

        NewFrame = Frame(self.MasterWindow,width=900,height=30,bg="white") 
        NewFrame.place(x=0,y=0) 

        for Index,Value in enumerate(self.Options):
            SetButton = Button(NewFrame,text=Value,bg="white",fg=self.PrimaryColours["ForegroundHiddenSharp"],relief="flat",font=self.FontLibrary["Helvetica_Options"]) 
            SetButton.place(x=10+(Index*80),y=3) #Padx could be increased 
            SetButton.bind("<Enter>", self.OnButtonEvent)
            SetButton.bind("<Leave>", self.OnButtonExit)

        #BorderSearch
        BorderContainerBar = Frame(NewFrame,width=319,height=25,relief="flat",bg=self.PrimaryColours["ForegroundActive"])
        BorderContainerBar.place(x=(self.Resolution[0]/2)-120,y=3)

        SearchEntryBar = Entry(BorderContainerBar,width=51,relief="flat",fg=self.PrimaryColours["ForegroundHiddenSharp"])
        SearchEntryBar.place(x=4,y=3)

        UserProfile = Frame(NewFrame,width=30,height=40,bg=self.PrimaryColours["ForegroundActive"])
        UserProfile.place(x=self.Resolution[0]-50,y=3)

        ProfileName = Label(NewFrame,width=10,height=1,text="Hello Dude!",bg="white",fg=self.PrimaryColours["ForegroundActive"],font=self.FontLibrary["Helvetica_Options"])
        ProfileName.place(x=self.Resolution[0]-130,y=5)

        #TEST!
        self.FrameFunctions["OrderFrame"]()

    def Update(self,Data):
        self.ItemNameTextBox.configure(text=f'This would give a price of {Data.Price*Data.Quantity}')

    #Frames: Would be controlled by the use of tablecommands
    def CreateOrderFrame(self):
        if (self.BaseFrame): self.BaseFrame.destroy()

        self.BaseFrame = Frame(self.MasterWindow,width=self.Resolution[0],height=self.Resolution[1],bg="white")
        self.BaseFrame.place(x=0,y=34)

        NewButton = Button(self.MasterWindow, width=14,height=1,text="Back To Menu",font=self.FontLibrary["Helvetica_Options"],bg=self.PrimaryColours["ForegroundActive"],relief="flat",fg="white",command= lambda: self.BaseWindowBuilder())
        NewButton.place(x=10,y=38)

        #EntryContainer - Input ItemName
        ItemNameTextBox = Label(self.MasterWindow,width=15,height=2,bg="white",fg=self.PrimaryColours["ForegroundHiddenSharp"],text="Your Item Name")
        ItemNameTextBox.place(x=0,y=75)

        ContainerItemEntryBox = Frame(self.MasterWindow,width=160,height=25,bg=self.PrimaryColours["ForegroundActive"])
        ContainerItemEntryBox.place(x=110,y=80)

        ItemEntryBox = Entry(ContainerItemEntryBox,width=25)
        ItemEntryBox.place(x=3,y=3)   

        #EntryContainer - Input Item Quantity
        ItemNameTextBox = Label(self.MasterWindow,width=15,height=2,bg="white",fg=self.PrimaryColours["ForegroundHiddenSharp"],text="Item Quantity")
        ItemNameTextBox.place(x=8,y=110)

        ContainerItemEntryBox = Frame(self.MasterWindow,width=160,height=25,bg=self.PrimaryColours["ForegroundActive"])
        ContainerItemEntryBox.place(x=110,y=115)

        ItemEntryBox = Entry(ContainerItemEntryBox,width=25)
        ItemEntryBox.place(x=3,y=3)   

        #EntryContainer - Input Item Price
        ItemNameTextBox = Label(self.MasterWindow,width=15,height=2,bg="white",fg=self.PrimaryColours["ForegroundHiddenSharp"],text="Item Price")
        ItemNameTextBox.place(x=16,y=145)

        ContainerItemEntryBox = Frame(self.MasterWindow,width=160,height=25,bg=self.PrimaryColours["ForegroundActive"])
        ContainerItemEntryBox.place(x=110,y=150)

        ItemEntryBox = Entry(ContainerItemEntryBox,width=25)
        ItemEntryBox.place(x=3,y=3)   

        #Confirmation of order price
        self.ItemNameTextBox = Label(self.MasterWindow,width=35,height=2,bg="white",fg=self.PrimaryColours["ForegroundHiddenSharp"],text="This would give a price of $Price$",font=self.FontLibrary["Helvetica_Italic"])
        self.ItemNameTextBox.place(x=2,y=185)

        Confirm = Button(self.MasterWindow, width=8,height=1,text="Confirm",font=self.FontLibrary["Helvetica_Options"],bg=self.PrimaryColours["ForegroundActive"],relief="flat",fg="white",command= lambda: self.BaseWindowBuilder())
        Confirm.place(x=230,y=190)


    def RenderCurrentOrderFrame(self):
        #Create the style for the treeview order window
        self.InstanceContainer = {}
        style = ttk.Style()
        style.configure("BW.TLabel", foreground="white", background="white")
        
        MainStyle = ttk.Style()
        MainStyle.configure("BW.TLabel",foreground=self.PrimaryColours["ForegroundActive"],background="white")

        #Create these first so we can attach elements to this (We can clear these later as one group)
        self.Taskbar = Frame(self.BaseFrame,height=self.Resolution[1]-38,width=150,bg="white")
        self.Taskbar.place(x=4,y=34)

        self.Titlebar = Frame(self.BaseFrame,height=40,width=self.Resolution[0]-166,bg="white")
        self.Titlebar.place(x=158,y=34)

        self.Basebar = Frame(self.BaseFrame,height=self.Resolution[0]-490,width=self.Resolution[0]-166,bg="white")
        self.Basebar.place(x=158,y=80)

        NoticeLabel = Label(self.Taskbar,text="Previous Orders",fg=self.PrimaryColours["ForegroundActive"],font=self.FontLibrary["Helvetica_Options"],bg="white")
        NoticeLabel.place(x=8,y=7)

        self.NewFrame = ttk.Treeview(self.Taskbar,height=10,style="BW.TLabel") 
        self.NewFrame.place(x=0,y=30)

        self.AddNewOrder = Button(self.Titlebar,width=15,height=1,relief="flat",font=self.FontLibrary["Helvetica_Button"],text="Create New Order",bg=self.PrimaryColours["ForegroundActive"],fg="white",command=lambda: self.FrameFunctions["CreateOrder"]())
        self.AddNewOrder.place(x=10,y=7)

        self.TitleText = Label(self.Basebar, width=15,height=2, text="My Current Orders",bg="white",fg=self.PrimaryColours["ForegroundActive"],font=self.FontLibrary["Helvetica_Title_Alternate"])
        self.TitleText.place(x=10,y=0)

        self.OrderContainer = ttk.Treeview(self.Basebar, height=100,style="BW.TLabel")#Preloaded style
        self.OrderContainer.place(x=10,y=40)

        self.OrderContainer.column('#0',width=145) 
        self.OrderContainer.heading("#0",text="Order Number") 

        self.OrderContainer['column'] = ['ItemName','Price','Quantity'] 
        self.OrderContainer.column('Price',width=145) 
        self.OrderContainer.heading("Price",text="Price") 

        self.OrderContainer.column('ItemName',width=145) 
        self.OrderContainer.heading("ItemName",text="Item Name") 

        self.OrderContainer.column('Quantity',width=145) 
        self.OrderContainer.heading("Quantity",text="Quantity")         

        for x in range(100):
            self.OrderContainer.insert(parent='',iid=x,text=x,index="end")




class OrderingSystem(Window): 
    NewOrderObjects = {} 

    def __init__(self): 
        self.Mode = "Get" 
        self.OrderNumberPriority = 0 
        Window.__init__(self) 

    #Program 
    def Order_Setter(self,Name,Price,Quantity): 
        self.OrderNumberPriority += 1 
        TableAppend = [] 
        TableAppend.append(float(Price)) 
        TableAppend.append(int(Quantity)) 
        TableAppend.append(str(Name)) 

        Window.OrderDatabase[self.OrderNumberPriority] = TableAppend 
        return Window.OrderDatabase[self.OrderNumberPriority] 

    def Order_Getter(self,Order): 
        return Window.OrderDatabase[int(Order)] 
 

if (__name__ == '__main__'): 
    NewOrder = OrderingSystem() 
    NewOrder.Order_Setter("Crisps",433,1) 
    NewOrder.Order_Setter("Chocolate",234,2) 
    NewOrder.MasterWindow.mainloop() 

 