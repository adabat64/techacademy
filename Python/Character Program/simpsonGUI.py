import wx, db_program

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title = title, size = (800,600))
        panel = wx.Panel(self) #initiating menu bar in panel

        #Menu Items
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        exitItem = fileMenu.Append(wx.NewId(), "Exit")
        menuBar.Append(fileMenu, "File")

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.exitProgram, exitItem)
        self.CreateStatusBar()

#UI addCharacter
            #Top text
        wx.StaticBox(panel, label='Add a new character', pos=(20, 40), size=(280,190))
            #Other text
        wx.StaticText(panel, label='Name', pos=(30, 70))
        wx.StaticText(panel, label='Gender', pos=(30, 110))
        wx.StaticText(panel, label='Age', pos=(30, 150))
        wx.StaticText(panel, label='Occupation', pos=(30, 190))

            #addCharacter Input Boxes
        self.sNam = wx.TextCtrl(panel, size=(150, -1), pos=(130, 70))
        self.sGen = wx.TextCtrl(panel, size=(150, -1), pos=(130, 110))
        self.sAge = wx.SpinCtrl(panel, value = '0', pos= (130,150), size=(70,25))
        self.sOcc = wx.TextCtrl(panel, size=(150, -1), pos=(130, 190))

        #addCharacter Button
        save = wx.Button(panel, label='Add Character', pos=(100,230))
        save.Bind(wx.EVT_BUTTON, self.addCharacter)

        # Setup the Table UI
            # Setup table as listCtrl
        self.listCtrl = wx.ListCtrl(panel, size=(400,400), pos=(350,40), style=wx.LC_REPORT |wx.BORDER_SUNKEN)

            # Add columns to listCtrl
        self.listCtrl.InsertColumn(0, "ID")
        self.listCtrl.InsertColumn(1, "Name")
        self.listCtrl.InsertColumn(2, "Gender")
        self.listCtrl.InsertColumn(3, "Age")
        self.listCtrl.InsertColumn(4, "Occupation")


        # Add data to the list control
        self.fillListCtrl()

        # Run onSelect function when item is selected
        self.listCtrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onSelect)

        # Setup a delete button
        deleteBtn = wx.Button(panel, label="Delete", pos=(640, 450))

        # Bind delete button to onDelete function
        deleteBtn.Bind(wx.EVT_BUTTON, self.onDelete)

        wx.StaticBox(panel, label='Update a character', pos=(20,340), size=(280,190))

        # Text for name, gender etc
        wx.StaticText(panel, label='Name:', pos=(30,370))
        wx.StaticText(panel, label='Gender:', pos=(30,410))
        wx.StaticText(panel, label='Age:', pos=(30,450))
        wx.StaticText(panel, label='Occupation:', pos=(30,490))

        # Single line text boxes
        self.sNameU = wx.TextCtrl(panel, size=(150, -1), pos=(130,370))
        self.sGenU = wx.TextCtrl(panel, size=(150, -1), pos=(130,410))
        self.sAgeU = wx.SpinCtrl(panel, value='0', pos=(130, 450), size=(70, 25))
        self.sOccU = wx.TextCtrl(panel, size=(150, -1), pos=(130,490))

        # Save button
        saveUpdate = wx.Button(panel, label="Update Character", pos=(100, 530))
        saveUpdate.Bind(wx.EVT_BUTTON, self.updateCharacter)

    def exitProgram(self, event):
        self.Destroy()

    def addCharacter(self, event):
        name = self.sNam.GetValue() #Getting the UI out for processing
        gen = self.sGen.GetValue()
        age = self.sAge.GetValue()
        occ = self.sOcc.GetValue()

        #Checking for blank input
        if (name == '') or (gen == '') or (age == ''):
            #Dialogue Box for user input
            dlg = wx.MessageDialog(None, 'Some Character details are missing', 'Enter values for all text boxes', 'Details missing', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()

        db_program.newCharacter(name, gen, age, occ)
        print db_program.viewAll()

        #Clear UI when done
        self.sNam.Clear()
        self.sGen.Clear()
        self.sAge.SetValue(0)
        self.sOcc.Clear()

        # Add data to the list control
        self.fillListCtrl()

    def fillListCtrl(self):
        # Get data from the database
        self.allData = db_program.viewAll()

        # Delete old data before adding new data
        self.listCtrl.DeleteAllItems()

        # Append data to the table
        for row in self.allData:
            # Loop though and append data
            self.listCtrl.Append(row)

    def onSelect(self, event):
        self.selectedId = event.GetText()        # Get index of selected row
        index = event.GetIndex()

        # Get character info
        charInfo = self.allData[index]
        print charInfo

        # Set value of update text boxes
        self.sNameU.SetValue(charInfo[1])
        self.sGenU.SetValue(charInfo[2])
        self.sAgeU.SetValue(charInfo[3])
        self.sOccU.SetValue(charInfo[4])

    def onDelete(self, event):
        db_program.deleteCharacter(self.selectedId)
        self.fillListCtrl()

    def updateCharacter(self, event):
        # Get the updated values
        name = self.sNameU.GetValue()
        gen = self.sGenU.GetValue()
        age = self.sAgeU.GetValue()
        occ = self.sOccU.GetValue()

        # Get character ID
        charId = self.selectedId

        # Update the character
        db_program.updateCharacter(charId, name, gen, age, occ)

        # Refresh list control
        self.fillListCtrl()

app = wx.App()
frame = Frame("Python GUI")
frame.Show()
app.MainLoop()
