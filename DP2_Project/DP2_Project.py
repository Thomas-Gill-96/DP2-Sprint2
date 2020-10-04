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

#test functionx
#def Lock_Text_Entry():
#	for entry in overlayElementsMasterFrame.winfo_children():
    		
		
#Ideally the above function would be written to lock user input when displaying the text entries
#however after too many days trying it is now down to an overload variable in Create_Sales_Record_List()



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
	global overlayElementsMasterFrame 
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
	stockOverlayFrame.pack_propagate(False)
	Generate_Text_Entry(stockOverlayFrame, "Date", CENTER, 5, (5, 5), 10)
	Create_Empty_Frame(stockOverlayFrame, 100)
	Generate_Text_Entry(stockOverlayFrame, "Stock Name", W, 5, (0, 5), 20)
	Create_Empty_Frame(stockOverlayFrame, 20)
	Generate_Text_Entry(stockOverlayFrame, "Stock Price", W, 5, (0, 5), 20)
	overlayElementsMasterFrame = stockOverlayFrame
	stockOverlayFrame.pack()
	

def Add_Sales_Record_Callback():
	global overlayElementsMasterFrame
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
	Generate_Text_Entry(stockOverlayFrame, "Date", CENTER, 5, (5, 5), 10)

	Create_Empty_Frame(stockOverlayFrame, 50)

	#Move to a function later
	zeroWidth = textHeaderFont.measure("0")

	#Header Frame
	labelWidth = (480/4)/zeroWidth
	#print(labelWidth)

	headerFrame = Frame(
		stockOverlayFrame,
		width = 480,
		height = 10,
		borderwidth = 2,
		relief = "ridge"
		)
	headerFrame.pack(fill = X)
	
	#Labels
	stockNameLabel = Label(
		headerFrame,
		text = "Stock Name",
		width = 13,
		font = textHeaderFont
		)
	stockPriceLabel = Label(
		headerFrame,
		text = "Price",
		width = 13,
		font = textHeaderFont
		)
	stockQuanityLabel = Label(
		headerFrame,
		text = "Quanity",
		width = 13,
		font = textHeaderFont
		)
	totalPriceLabel = Label(
		headerFrame,
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

	overlayContentFrame = Frame(
		stockOverlayFrame,
		width = 480
		)
	overlayContentFrame.pack(fill = X)
	overlayElementsMasterFrame = overlayContentFrame
	#Call to the function that selects and genegates the text entry boxes
	Create_Sales_Record_List(overlayContentFrame)

	stockOverlayFrame.pack()

def Edit_Sales_Record_Callback():
	global overlayElementsMasterFrame
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
	Generate_Text_Entry(stockOverlayFrame, "Date", CENTER, 5, (5, 5), 10)
	stockOverlayFrame.pack()

def Display_Sales_Record_Callback():
	
	global overlayElementsMasterFrame
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

	overlayElementsMasterFrame = stockOverlayFrame
	Generate_Text_Entry(stockOverlayFrame, "Date", CENTER, 5, (5, 5), 10)


	Create_Empty_Frame(stockOverlayFrame, 50)
	
	#Move to a function later
	zeroWidth = textHeaderFont.measure("0")\
	
	#Header Frame
	labelWidth = (480/4)/zeroWidth
	#print(labelWidth)
	headerFrame = Frame(
		stockOverlayFrame,
		width = 480,
		height = 10,
		borderwidth = 2,
		relief = "ridge"
		)
	headerFrame.pack(fill = X)

	#Labels
	stockNameLabel = Label(
		headerFrame,
		text = "Stock Name",
		width = 13,
		font = textHeaderFont
		)
	stockPriceLabel = Label(
		headerFrame,
		text = "Price",
		width = 13,
		font = textHeaderFont
		)
	stockQuanityLabel = Label(
		headerFrame,
		text = "Quanity",
		width = 13,
		font = textHeaderFont
		)
	totalPriceLabel = Label(
		headerFrame,
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

	#List Stuff
	Create_Sales_Record_List(stockOverlayFrame, 1)#the 1 is an oveload to set the text entry fields to disabled


	#Lock_Text_Entry() Function incomplete, and now optional. delete if not used

	stockOverlayFrame.pack()

def Generate_Sales_Report_Callback():
	global overlayElementsMasterFrame
	global acceptState
	acceptState = 5

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
	Generate_Text_Entry(stockOverlayFrame, "Date", CENTER, 5, (5, 5), 10)
	stockOverlayFrame.pack()

def Accept_Button_Callback():
	global acceptState
	widgets = overlayElementsMasterFrame.winfo_children()
	Entries = list()
	
	
	if acceptState == 1:
		for widget in widgets:
			if widget.winfo_class() == 'Entry':
				Entries.append(widget.get())
		# call add item function
		print(Entries[1])
		print(Entries[2])
		InsertItem(Entries[1], Entries[2])
	elif acceptState == 2:
		tempList = list()
		for rowFrame in widgets:
			tempList.clear()
			print("Inside elements master frame")
			print(rowFrame.winfo_class())
			if rowFrame.winfo_class() == 'Frame':
				for entry in rowFrame.winfo_children():
					if((entry.winfo_class() == "Entry") and (entry.get() != "")):
						tempList.append(entry.get())
			#addToSales("02/10/2020", tempList[0], tempList[2], tempList[3])
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

#Overlay Elements Master Frame Reference
overlayElementsMasterFrame = Frame()

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
buttonFont = ("Avenir", "14")
headingFont = ("Avenir", "26", "bold")
subHeadingFont = ("Avenir", "20", "bold")
#dateFont = ("Avenir", "18") If we end up doing a calender drop down box
textFont = ("Avenir", "12")
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