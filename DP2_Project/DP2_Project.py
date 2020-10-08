from tkinter import *
#from InsertItem import *
from Database_Queries import *
import tkinter.font as tkfont

#Function Declarations

#Clear Overlay Screen
def Clear_Overlay():
	for x in overlayFrame.winfo_children():
		x.destroy()

#Create an Empty Frame or Spacer
def Create_Empty_Frame(masterFrame, paddingY):
	tempFrame = Frame(
		masterFrame,
		height = paddingY,
		borderwidth = 5,
		relief = "ridge"
		)
	tempFrame.pack_propagate(False)
	tempFrame.pack()

#Generic Title Creation for Overlay Screens
def Title_Label_Creation(titleName):
	tempTitleLabel = Label(
		overlayFrame,
		text = titleName,
		font = subHeadingFont
		)
	tempTitleLabel.pack(fill=BOTH, pady = (30, 10))

def Update_Exclusive_Buttons():
	global reportOptionButtonState

	buttons = list()
	contentFrames = overlayElementsContentFrame.winfo_children()
	for buttonFrame in contentFrames:
		for button in buttonFrame.winfo_children():
			buttons.append(button)

	if(reportOptionButtonState == False):
		print("Weekly Report Selected")
		#Active Button
		buttons[0]['bg'] = LIGHTERGRAY
		buttons[0]['relief'] = 'sunken'
		buttons[0]['state'] = DISABLED

		#Non-active Button
		buttons[1]['bg'] = LIGHTGRAY
		buttons[1]['relief'] = 'raised'
		buttons[1]['state'] = NORMAL
	elif(reportOptionButtonState):
		print("Monthly Report Selected")
		
		#Non-active Button
		buttons[0]['bg'] = LIGHTGRAY
		buttons[0]['relief'] = 'raised'
		buttons[0]['state'] = NORMAL
		
		#Active Button
		buttons[1]['bg'] = LIGHTERGRAY
		buttons[1]['relief'] = 'sunken'
		buttons[1]['state'] = DISABLED


#Generates an entry field, along with a label for the entry
def Generate_Text_Entry(masterFrame, labelTitle, anchoredPos, paddingX, paddingY, textBoxLength):
	tempLabel = Label(
		masterFrame,
		text = labelTitle,
		font = buttonFont
		)
		
	tempEntry = Entry(
		masterFrame,
		width = textBoxLength,
		borderwidth = 2,
		relief = "sunken",
		font = textFont
		)
	tempLabel.pack(anchor = anchoredPos, padx = paddingX, pady = paddingY)
	tempEntry.pack(anchor = anchoredPos, padx = paddingX, pady = paddingY)

	return tempEntry

def Unlock_Accept_Button():
	for button in subMenuFrame.winfo_children():
		if(button['text'] == "Accept"):
			button['state'] = NORMAL
			break

def Unlock_Cancel_Button():
	for button in subMenuFrame.winfo_children():
		if(button['text'] == "Cancel"):
			button['state'] = NORMAL
			break

def Unlock_Export_Button():
	for button in subMenuFrame.winfo_children():
		if(button['text'] == "Export"):
			button['state'] = NORMAL
			break

def Lock_Sub_Buttons():
	for button in subMenuFrame.winfo_children():
		button['state'] = DISABLED

#this funtion targets the entries (text inputs) on display record page
# default toggles the state between DISABLED and NORMAL
# call with lock, unlock to choose 'state' to set
def Change_Entry_State(desiredState = 'toggle'):
	widgets = overlayElementsContentFrame.winfo_children()
	entries = []
	#print(widgets)
	for rowFrame in widgets:
    		if(rowFrame.winfo_class() == "Frame"):
    				for entry in rowFrame.winfo_children():
    						if(entry.winfo_class() == "Entry"):
    							entries.append(entry)
	
	for selected in entries:
    		if(desiredState == 'toggle'):
    				if(selected['state'] == NORMAL):
        						selected['state'] = DISABLED
    				elif(selected['state'] == DISABLED):
    						selected['state'] = NORMAL
    		elif(desiredState == 'unlock'):
    				selected['state'] = NORMAL
    		elif(desiredState == 'lock'):
    				selected['state'] = DISABLED



def Create_Sales_Record_Row(masterFrame, stockName, stockPrice, stockQuanity, totalPrice, paddingX, paddingY):
	
	#Frame
	headerFrame1 = Frame(
		masterFrame,
		width = 480,
		height = 10,
		borderwidth = 2,
		relief = "ridge"
		)
	headerFrame1.pack(fill = X)

	#Entries
	itemClicked = StringVar()
	itemList = SelectItemNames() 
	stockNameLabel1 = OptionMenu(
		headerFrame1,
		itemClicked,
		*itemList
		)
	stockPriceLabel1 = Entry(
		headerFrame1,
		width = 1,
		font = buttonFont
		)
	
	stockQuanityLabel1 = Entry(
		headerFrame1,
		width = 1,
		font = buttonFont
		)
	totalPriceLabel1 = Entry(
		headerFrame1,
		width = 1,
		font = buttonFont
		)
	
	stockNameLabel1.pack(side = LEFT, fill = X, anchor = CENTER, expand = 2.5)
	stockPriceLabel1.pack(side = LEFT, fill = X, anchor = CENTER, expand = 1.0)
	stockQuanityLabel1.pack(side = LEFT, fill = X, anchor = CENTER, expand = 1.0)
	totalPriceLabel1.pack(side = LEFT, fill = X, anchor = CENTER, expand = 1.5)


	#print("Created a row of entries")


#this version is only called by display sales record so far
def Create_Locked_Sales_Record_Row(masterFrame, stockName, stockPrice, stockQuanity, totalPrice, paddingX, paddingY):

	#Frame	
	headerFrame1 = Frame(
		masterFrame,
		width = 480,
		height = 10,
		borderwidth = 2,
		relief = "ridge"
		)
	headerFrame1.pack(fill = X)

	#Entries
	stockNameLabel1 = Entry(
		headerFrame1,
		width = 1,
		font = buttonFont
		)
	
	stockPriceLabel1 = Entry(
		headerFrame1,
		width = 1,
		font = buttonFont
		)
	
	stockQuanityLabel1 = Entry(
		headerFrame1,
		width = 1,
		font = buttonFont
		)
	totalPriceLabel1 = Entry(
		headerFrame1,
		width = 1,
		font = buttonFont
		)

	stockNameLabel1['state'] = DISABLED
	stockPriceLabel1['state'] = DISABLED
	stockQuanityLabel1['state'] = DISABLED
	totalPriceLabel1['state'] = DISABLED

	stockNameLabel1.pack(side = LEFT, fill = X, anchor = CENTER, expand = 2.5)
	stockPriceLabel1.pack(side = LEFT, fill = X, anchor = CENTER, expand = 1.0)
	stockQuanityLabel1.pack(side = LEFT, fill = X, anchor = CENTER, expand = 1.0)
	totalPriceLabel1.pack(side = LEFT, fill = X, anchor = CENTER, expand = 1.5)

def Create_Sales_Record_List(masterFrame , locked = 0):
	#print(locked)

	for x in range(0, 4):
		#add if to sleect open or locked
		if(locked == 1):
			Create_Locked_Sales_Record_Row(masterFrame, x, "", x, "", 20, 10)
		else:
			Create_Sales_Record_Row(masterFrame, x, "", x, "", 20, 10)
	

def Add_Stock_Callback():
	global acceptState
	acceptState = 1
	global overlayElementsHeaderFrame 
	global overlayElementsContentFrame
	Clear_Overlay()

	Unlock_Accept_Button()
	Unlock_Cancel_Button()

	Title_Label_Creation("Add a Stock Item")
	stockOverlayFrame = Frame(
		overlayFrame,
		width = 480,
		height = 600,
		borderwidth = 5,
		relief = "ridge"
		)
	
	overlayHeaderFrame = Frame(
		stockOverlayFrame,
		width = 480
		)
	#Not Currently Used
	#overlayHeaderFrame.pack(fill = X)

	overlayContentFrame = Frame(
		stockOverlayFrame,
		width = 480
		)
	overlayContentFrame.pack(fill = X)

	stockOverlayFrame.pack_propagate(False)
	#Generate_Text_Entry(stockOverlayFrame, "Date", CENTER, 5, (5, 5), 10)
	Create_Empty_Frame(overlayContentFrame, 100)
	Generate_Text_Entry(overlayContentFrame, "Stock Name", W, 5, (0, 5), 20)
	Create_Empty_Frame(overlayContentFrame, 20)
	Generate_Text_Entry(overlayContentFrame, "Stock Price", W, 5, (0, 5), 20)
	
	overlayElementsHeaderFrame = overlayHeaderFrame
	overlayElementsContentFrame = overlayContentFrame

	stockOverlayFrame.pack()
	

def Add_Sales_Record_Callback():
	global overlayElementsHeaderFrame 
	global overlayElementsContentFrame
	global acceptState
	acceptState = 2
	Clear_Overlay()
	Lock_Sub_Buttons()
	Unlock_Accept_Button()
	Unlock_Cancel_Button()

	print("Adding a sales record....")
	Title_Label_Creation("Add a Sales Record")
	stockOverlayFrame = Frame(
		overlayFrame,
		width = 480,
		height = 600,
		borderwidth = 5,
		relief = "ridge"
		)
	stockOverlayFrame.pack_propagate(False)

	overlayHeaderFrame = Frame(
		stockOverlayFrame,
		width = 480
		)
	overlayHeaderFrame.pack(fill = X)

	overlayContentFrame = Frame(
		stockOverlayFrame,
		width = 480
		)
	overlayContentFrame.pack(fill = X)

	Generate_Text_Entry(overlayHeaderFrame, "Date", CENTER, 5, (5, 5), 10)

	Create_Empty_Frame(overlayHeaderFrame, 50)

	#Move to a function later
	zeroWidth = textHeaderFont.measure("0")

	#Header Frame
	labelWidth = (480/4)/zeroWidth
	#print(labelWidth)
	
	#Labels
	stockNameLabel = Label(
		overlayHeaderFrame,
		text = "Stock Name",
		width = 13,
		font = textHeaderFont
		)
	stockPriceLabel = Label(
		overlayHeaderFrame,
		text = "Price",
		width = 13,
		font = textHeaderFont
		)
	stockQuanityLabel = Label(
		overlayHeaderFrame,
		text = "Quanity",
		width = 13,
		font = textHeaderFont
		)
	totalPriceLabel = Label(
		overlayHeaderFrame,
		text = "Total",
		width = 13,
		font = textHeaderFont
		)
	stockNameLabel.pack_propagate(False)
	stockPriceLabel.pack_propagate(False)
	stockQuanityLabel.pack_propagate(False)
	totalPriceLabel.pack_propagate(False)
	stockNameLabel.pack(side = LEFT, anchor = CENTER)
	stockPriceLabel.pack(side = LEFT, anchor = CENTER)
	stockQuanityLabel.pack(side = LEFT, anchor = CENTER)
	totalPriceLabel.pack(side = LEFT, anchor = CENTER)

	overlayElementsHeaderFrame = overlayHeaderFrame
	overlayElementsContentFrame = overlayContentFrame

	#Call to the function that selects and genegates the text entry boxes
	Create_Sales_Record_List(overlayContentFrame)

	stockOverlayFrame.pack()

def Edit_Sales_Record_Callback():
	global overlayElementsHeaderFrame 
	global overlayElementsContentFrame
	global acceptState
	acceptState = 3

	Clear_Overlay()
	Lock_Sub_Buttons()
	Unlock_Accept_Button()
	Unlock_Cancel_Button()

	print("Editing a sales record....")
	Title_Label_Creation("Edit a Sales Record")
	stockOverlayFrame = Frame(
		overlayFrame,
		width = 480,
		height = 600,
		borderwidth = 5,
		relief = "ridge"
		)
	stockOverlayFrame.pack_propagate(False)

	overlayHeaderFrame = Frame(
		stockOverlayFrame,
		width = 480
		)
	overlayHeaderFrame.pack(fill = X)

	overlayContentFrame = Frame(
		stockOverlayFrame,
		width = 480
		)
	overlayContentFrame.pack(fill = X)

	overlayElementsHeaderFrame = overlayHeaderFrame
	overlayElementsContentFrame = overlayContentFrame

	stockOverlayFrame.pack()

def Display_Sales_Record_Callback():
	
	global overlayElementsHeaderFrame 
	global overlayElementsContentFrame
	global acceptState
	acceptState = 4

	Clear_Overlay()
	Lock_Sub_Buttons()
	Unlock_Accept_Button()
	Unlock_Cancel_Button()
	Unlock_Export_Button()

	print("Displaying a sales record....")
	Title_Label_Creation("Sales Record")
	stockOverlayFrame = Frame(
		overlayFrame,
		width = 480,
		height = 600,
		borderwidth = 5,
		relief = "ridge"
		)
	stockOverlayFrame.pack_propagate(False)

	overlayHeaderFrame = Frame(
		stockOverlayFrame,
		width = 480
		)
	overlayHeaderFrame.pack(fill = X)

	overlayContentFrame = Frame(
		stockOverlayFrame,
		width = 480
		)
	overlayContentFrame.pack(fill = X)

	Generate_Text_Entry(overlayHeaderFrame, "Date", CENTER, 5, (5, 5), 10)


	Create_Empty_Frame(overlayHeaderFrame, 50)
	
	#Move to a function later
	zeroWidth = textHeaderFont.measure("0")\
	
	#Header Frame
	labelWidth = (480/4)/zeroWidth
	#print(labelWidth)

	#Labels
	stockNameLabel = Label(
		overlayHeaderFrame,
		text = "Stock Name",
		width = 13,
		font = textHeaderFont
		)
	stockPriceLabel = Label(
		overlayHeaderFrame,
		text = "Price",
		width = 13,
		font = textHeaderFont
		)
	stockQuanityLabel = Label(
		overlayHeaderFrame,
		text = "Quanity",
		width = 13,
		font = textHeaderFont
		)
	totalPriceLabel = Label(
		overlayHeaderFrame,
		text = "Total",
		width = 13,
		font = textHeaderFont
		)
	stockNameLabel.pack_propagate(False)
	stockPriceLabel.pack_propagate(False)
	stockQuanityLabel.pack_propagate(False)
	totalPriceLabel.pack_propagate(False)
	stockNameLabel.pack(side = LEFT, anchor = CENTER)
	stockPriceLabel.pack(side = LEFT, anchor = CENTER)
	stockQuanityLabel.pack(side = LEFT, anchor = CENTER)
	totalPriceLabel.pack(side = LEFT, anchor = CENTER)

	Create_Sales_Record_List(overlayContentFrame)

	overlayElementsHeaderFrame = overlayHeaderFrame
	overlayElementsContentFrame = overlayContentFrame

	#this function can be called without params to toggle state, or with the text 'lock' or 'unlock'
	Change_Entry_State('lock')

	stockOverlayFrame.pack()

def Generate_Sales_Report_Callback():
	global overlayElementsHeaderFrame 
	global overlayElementsContentFrame
	global reportOptionButtonState
	global acceptState
	acceptState = 5
	reportOptionButtonState = False
	buttonWidth = 12
	buttonHeight = 2.5

	buttonWidthPixelRatio = buttonFont.measure("0")
	buttonHeightPixelRatio = buttonFont.metrics('linespace')

	Clear_Overlay()
	Lock_Sub_Buttons()
	Unlock_Accept_Button()
	Unlock_Cancel_Button()
	Unlock_Export_Button()

	print("Generating Sales Report....")
	Title_Label_Creation("Sales Report")

	stockOverlayFrame = Frame(
		overlayFrame,
		width = 480,
		height = 600,
		borderwidth = 5,
		relief = "ridge"
		)
	stockOverlayFrame.pack_propagate(False)

	overlayHeaderFrame = Frame(
		stockOverlayFrame,
		width = 480
		)
	overlayHeaderFrame.pack(fill = X)

	overlayContentFrame = Frame(
		stockOverlayFrame,
		width = 480
		)
	overlayContentFrame.pack(fill = X)

	Generate_Text_Entry(overlayHeaderFrame, "Date", CENTER, 5, (5, 5), 10)

	buttonFrame = Frame(
		overlayContentFrame,
		width = (2*buttonWidth*buttonWidthPixelRatio),
		height = (buttonHeight*buttonHeightPixelRatio),
		borderwidth = 1,
		relief = "sunken",
		bg = LIGHTGRAY
		)
	buttonFrame.pack_propagate(False);
	buttonFrame.pack()

	weeklyButton = Button(
		buttonFrame,
		text = "Weekly",
		width = buttonWidth,
		height = 3,
		relief = "sunken",
		font = buttonFont,
		bg = LIGHTERGRAY,
		activebackground = LIGHTERGRAY,
		fg = ALMOSTBLACK,
		disabledforeground = ALMOSTBLACK,
		state = DISABLED,
		command = Weekly_Button_Callback
		)
	weeklyButton.pack(side = LEFT)

	monthlyButton = Button(
		buttonFrame,
		text = "Monthly",
		width = buttonWidth,
		height = 3,
		relief = "raised",
		font = buttonFont,
		bg = LIGHTGRAY,
		activebackground = LIGHTERGRAY,
		#disabledbackground = LIGHTERGRAY,
		fg = ALMOSTBLACK,
		disabledforeground = ALMOSTBLACK,
		state = NORMAL,
		command = Monthly_Button_Callback
		)
	monthlyButton.pack(side = LEFT)

	overlayElementsHeaderFrame = overlayHeaderFrame
	overlayElementsContentFrame = overlayContentFrame

	stockOverlayFrame.pack()

def Accept_Button_Callback():
	global acceptState
	#widgets = overlayElementsMasterFrame.winfo_children()
	
	headerWidgets = overlayElementsHeaderFrame.winfo_children() #Note this includes Frames
	contentWidgets = overlayElementsContentFrame.winfo_children() #Note this includes Frames
	
	Entries = list()
	
	
	if acceptState == 1:
		for widget in contentWidgets:
			if widget.winfo_class() == 'Entry':
				Entries.append(widget.get())
		# call add item function
		print(Entries[0])
		print(Entries[1])
		InsertItem(Entries[1], Entries[1])
	elif acceptState == 2:
		tempList = list()

		for widget in headerWidgets:
			if(widget.winfo_class() == 'Entry'):
				date = widget.get()


		for rowFrame in contentWidgets:
			tempList.clear()
			print(rowFrame.winfo_class())
			if rowFrame.winfo_class() == 'Frame':
				for entry in rowFrame.winfo_children():
					if((entry.winfo_class() == "Entry") and (entry.get() != "")):
						tempList.append(entry.get())
			#addToSales(date, tempList[0], tempList[2], tempList[3])
			print(tempList)
		print("Added Sales Record")

	elif acceptState == 3:
		print("Editing a Sales Record")
	elif acceptState == 4:
		print("Displaying a Sales Record")
	elif acceptState == 5:
		print("Generating Sales Report")

	Clear_Overlay()
	Lock_Sub_Buttons()
	print("I Accepted Something")

	

def Cancel_Button_Callback():
	print("I Canceled Something")
	Clear_Overlay()
	Lock_Sub_Buttons()

def Export_Button_Callback():
	print("I Exported Something")
	Clear_Overlay()
	Lock_Sub_Buttons()

def Weekly_Button_Callback():
	global reportOptionButtonState

	reportOptionButtonState = 0
	Update_Exclusive_Buttons()

def Monthly_Button_Callback():
	global reportOptionButtonState

	reportOptionButtonState = 1
	Update_Exclusive_Buttons()

#Generates and fills content for the title frame
def Initialise_Title_Frame():
	titleLabel = Label(
	master=titleFrame,
	text = "People Health Pharmacy Inc.",
	font = headingFont
	)
	titleLabel.pack()

def Initialise_Side_Menu_Frame():
	#Frame for Logo
	logoFrame = Frame(sideBarFrame)
	logoFrame.pack()
	#Logo Creation
	logoLabel = Label(
		master = logoFrame,
		image = phpLogo
		)
	logoLabel.pack(pady = (30,50))

	#Main Menu Buttons
	mainMenuButtonsFrame = Frame(sideBarFrame)

	#Add Stock Item Button
	addStockButton = Button(
		master=mainMenuButtonsFrame,
		text = "Add a Stock Item",
		width = 20,
		height = 3,
		font = buttonFont,
		bg = LIGHTGRAY,
		fg = ALMOSTBLACK,
		command = Add_Stock_Callback
		)
	addStockButton.pack(padx = 15, pady = 10)

	#Add Sales Record Button
	addSalesRecordButton = Button(
		master=mainMenuButtonsFrame,
		text = "Add a Sales Record",
		width = 20,
		height = 3,
		font = buttonFont,
		bg = LIGHTGRAY,
		fg = ALMOSTBLACK,
		command = Add_Sales_Record_Callback
		)
	addSalesRecordButton.pack(padx = 15, pady = 10)

	#Edit Sales Record Button
	editSalesRecordButton = Button(
		master=mainMenuButtonsFrame,
		text = "Edit a Sales Record",
		width = 20,
		height = 3,
		font = buttonFont,
		bg = LIGHTGRAY,
		fg = ALMOSTBLACK,
		command = Edit_Sales_Record_Callback
		)
	editSalesRecordButton.pack(padx = 15, pady = 10)

	#Display Sales Record Button
	displaySalesRecordButton = Button(
		master=mainMenuButtonsFrame,
		text = "Display a Sales Record",
		width = 20,
		height = 3,
		font = buttonFont,
		bg = LIGHTGRAY,
		fg = ALMOSTBLACK,
		command = Display_Sales_Record_Callback
		)
	displaySalesRecordButton.pack(padx = 15, pady = 10)

	#Generate Report Button
	generateReportButton = Button(
		master=mainMenuButtonsFrame,
		text = "Generate a Sales Report",
		width = 20,
		height = 3,
		font = buttonFont,
		bg = LIGHTGRAY,
		fg = ALMOSTBLACK,
		command = Generate_Sales_Report_Callback
	)
	generateReportButton.pack(padx = 15, pady = 10)
	
	mainMenuButtonsFrame.pack()

#Generate Sub Menu
def Initialise_Sub_Menu_Frame():
	exportButton  = Button(
		master = subMenuFrame,
		text = "Export",
		width = 20,
		height = 3,
		font = buttonFont,
		bg = LIGHTGRAY,
		fg = ALMOSTBLACK,
		state = DISABLED,
		command = Export_Button_Callback
		)
	exportButton.pack(side = LEFT, anchor = W)

	cancelButton  = Button(
		master = subMenuFrame,
		text = "Cancel",
		width = 20,
		height = 3,
		font = buttonFont,
		bg = LIGHTGRAY,
		fg = ALMOSTBLACK,
		state = DISABLED,
		command = Cancel_Button_Callback
		)
	cancelButton.pack(side = LEFT, anchor = CENTER)

	AcceptButton  = Button(
		master = subMenuFrame,
		text = "Accept",
		width = 20,
		height = 3,
		font = buttonFont,
		bg = LIGHTGRAY,
		fg = ALMOSTBLACK,
		state = DISABLED,
		command = Accept_Button_Callback
		)
	AcceptButton.pack(side = LEFT,anchor = E)

#Constants
LIGHTERGRAY = "#cccccc"
LIGHTGRAY = "#a6a6a6"
ALMOSTBLACK = "#292929"

#Global Varaibles
root = Tk()
root.geometry('1280x960')
phpLogo = PhotoImage(file="images/logo2.png")
#overlayFrameList = [] No used anymore, Delete if no use is found
overlayListElements = [4]
print(overlayListElements)
acceptState = 0
reportOptionButtonState = bool

#Overlay Elements Master Frame Reference
overlayElementsHeaderFrame = Frame()
overlayElementsContentFrame = Frame()

#Title Frame Creation
titleFrame = Frame(
	root,
    width = 800,
    height = 60,
    borderwidth = 5,
	relief = "ridge"
	)

#Side Menu Creation
sideBarFrame = Frame(
	root,
	height = 900,
	borderwidth = 5,
	relief = "ridge"
	)

#Overlay Area Creation
overlayFrame = Frame(
    root,
    width = 800,
    height = 750,
    borderwidth = 5,
	relief = "ridge"
    )

#Sub Menu Creation (Bottom Menu)
subMenuFrame = Frame(
	root,
	width = 800,
    height = 150,
    borderwidth = 5,
	relief = "ridge"
	)

#Fonts
#buttonFont = ("Avenir", "14")
buttonFont = tkfont.Font(family="Avenir", size=14, weight="normal")
headingFont = tkfont.Font(family="Avenir", size=26, weight="bold") #("Avenir", "26", "bold")
subHeadingFont = tkfont.Font(family="Avenir", size=20, weight="bold") #("Avenir", "20", "bold")
#dateFont = ("Avenir", "18") If we end up doing a calender drop down box
textFont = tkfont.Font(family="Avenir", size=12, weight="normal") #("Avenir", "12")
#textHeaderFont = ("Avenir", "12", "bold")
textHeaderFont = tkfont.Font(family="Avenir", size=12, weight="bold")

#Frame Intialisation
Initialise_Title_Frame()
Initialise_Side_Menu_Frame()
Initialise_Sub_Menu_Frame()




#Pack Order
sideBarFrame.pack(side = LEFT, fill = BOTH)
titleFrame.pack(fill = BOTH)
overlayFrame.pack(fill = BOTH, expand = 1)
subMenuFrame.pack_propagate(False)
subMenuFrame.pack(fill = BOTH)

root.mainloop()