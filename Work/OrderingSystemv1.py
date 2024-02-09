from tkinter import * 
from tkinter import ttk 
from tkinter import font 

#Will clean this up later.
class Window: 
    OrderDatabase = {} 
    def __init__(self): 
        self.MasterWindow = Tk() 
        self.FrameConfigurationsBuilder() 
        self.CreateNewWindow() 


    #Building the new frame
    def FrameConfigurationsBuilder(self): 
        self.MasterWindow.geometry("600x300") 
        self.MasterWindow.maxsize(600,300) 
        self.MasterWindow.minsize(600,300) 

        self.CurrentWindow = None 
        self.FontLibrary = { 
            "Helvetica_Options":font.Font(family='Helvetica', size=9, weight='bold'), 
            "Helvetica":font.Font(family="Helvetica",size=9),
            "Helvetica_Title":font.Font(family='Helvetica', size=12, weight='bold'), 
        } 

    def CreateNewOrder(self,MainFrame):
        if (self.CreationButton):
            self.CreationButton.destroy()

        Notify1 = Label(MainFrame,bg="white",width=20,height=1,text="Your Order Name",font=self.FontLibrary["Helvetica"])
        Notify1.place(x=0,y=30)
        Notify1 = Label(MainFrame,bg="white",width=20,height=1,text="Order Quantity",font=self.FontLibrary["Helvetica"])
        Notify1.place(x=0,y=60)
      
        InputTextbox = Text(MainFrame,width=15,height=1)
        InputTextbox.place(x=130,y=30)

        InputTextboxQuantity = Text(MainFrame,width=15,height=1)
        InputTextboxQuantity.place(x=130,y=60)

    #Generates frames and binds to input.
    def GenerateData(self): 
        if (not self.NewFrame): return 
        if (self.Mode == "Get"):  
            for Index,Instances in enumerate(Window.OrderDatabase.values()): 
                self.NewFrame.insert(parent='',iid=Index, text="#"+str(Index+1),values=[Instances[2],"£"+str(Instances[0]),"x"+str(Instances[1])], index='end',) 
                self.NewFrame.bind("<Button-1>")

    #Does whatever the mode is set towards.
    def UIControl(self,Mode): 
        if (self.CurrentWindow): 
            self.CurrentWindow.destroy() 

        self.Mode = Mode 
        if (self.Mode == "Get"): 
            self.CurrentWindow = Frame(self.MasterWindow,width=600,height=500,background="#ffffff") 
            self.CurrentWindow.place(x=0,y=30) 

            Title = Label(self.CurrentWindow,text="Current Orders",font=self.FontLibrary["Helvetica_Title"],background='#ffffff') 
            Title.place(x=10,y=4) 

            self.NewFrame = ttk.Treeview(self.CurrentWindow,height=10) 
            self.NewFrame.column('#0',width=145) 
            self.NewFrame.heading("#0",text="Order Number") 

            self.NewFrame['column'] = ['ItemName','Price','Quantity'] 
            self.NewFrame.column('Price',width=145) 
            self.NewFrame.heading("Price",text="Price") 

            self.NewFrame.column('ItemName',width=145) 
            self.NewFrame.heading("ItemName",text="Item Name") 

            self.NewFrame.column('Quantity',width=145) 
            self.NewFrame.heading("Quantity",text="Quantity") 

            self.NewFrame.place(x=10,y=30) 

        elif (self.Mode == "Set"): 
            self.CurrentWindow = Frame(self.MasterWindow,width=600,height=500,background="#ffffff") 
            self.CurrentWindow.place(x=0,y=30) 

            Title = Label(self.CurrentWindow,text="Create An Order",font=self.FontLibrary["Helvetica_Title"],background='#ffffff') 
            Title.place(x=10,y=4) 

            self.CreationButton = Button(self.CurrentWindow,text="Create Order",relief="groove",command= lambda: self.CreateNewOrder(self.CurrentWindow)) 
            self.CreationButton.place(x=260,y=30) 
        elif (self.Mode == "View"):
            self.CurrentWindow = Frame(self.MasterWindow, width=600, height=500, background="#ffffff")
            self.CurrentWindow.place(x=0,y=0)


    def CreateNewWindow(self): 
        NewFrame = Frame(self.MasterWindow,width=900,height=30,bg='#454343') 
        NewFrame.place(x=0,y=0) 

        SetButton = Button(self.MasterWindow,text="Set Order",bg="#454343",fg="white",relief="flat",font=self.FontLibrary["Helvetica_Options"],command = lambda: self.UpdateWindow("Get")) 
        SetButton.place(x=90,y=3) 

        GetButton = Button(self.MasterWindow,text="Get Order",bg="#454343",fg="white",relief="flat",font=self.FontLibrary["Helvetica_Options"],command = lambda: self.UpdateWindow("Set")) 
        GetButton.place(x=10,y=3)    

        self.UpdateWindow("Get") 

    def UpdateWindow(self,Mode): 
        self.UIControl(Mode) 
        self.GenerateData() 


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
        self.UpdateWindow(self.Mode)
        return Window.OrderDatabase[self.OrderNumberPriority] 

    def Order_Getter(self,Order): 
        return Window.OrderDatabase[int(Order)] 
 

if (__name__ == '__main__'): 
    NewOrder = OrderingSystem() 
    NewOrder.Order_Setter("Crisps",433,1) 
    NewOrder.Order_Setter("Chocolate",234,2) 
    NewOrder.MasterWindow.mainloop() 

 