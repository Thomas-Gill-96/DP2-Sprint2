from tkinter import *
#from InsertItem import *
from Database_Queries import *
import tkinter.font as tkfont
from ExportCSV import *

aItemName = ""
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
def Generate_Text_Entry(masterFrame, labelTitle, anchoredPos, paddingX, paddingY, textBoxLength, date = ''):
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
		font = textFont,
		)
	tempEntry.insert(0, date)
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

def Unlock_Edit_Button():
	for button in subMenuFrame.winfo_children():
		if(button['text'] == "Edit"):
			button['state'] = NORMAL
			break

def Lock_Sub_Buttons():
	for button in subMenuFrame.winfo_children():
		button['state'] = DISABLED

#this funtion targets the entries (text inputs) on display record page
# default toggles the state between DISABLED and NORMAL
# call with lock, unlock to choose 'state' to set
def Change_Entry_State(desiredState = 'toggle'):
	global overlayElementsContentFrame
	widgets = overlayElementsContentFrame.winfo_children()
	#print(widgets)
	entries = []
	for rowFrame in widgets:
    		if(rowFrame.winfo_class() == "Frame"):
    				for entry in rowFrame.winfo_children():
    						if(entry.winfo_class() == "Entry"):
    							entries.append(entry)
	
	#print(entries)
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
	itemList = SelectItemNames() 
	itemPriceList = SelectItemPrices()
	itemClicked = StringVar()
	itemClicked.set(itemList[0])
	
	stockNameLabel1 = OptionMenu(
		headerFrame1,
		itemClicked,
		*itemList,
		command = Update_Price
		)	
	#Update_Price(itemList[0])
	#Update_Price(itemClicked)

	stockPriceLabel1 = Entry(
		headerFrame1,
		width = 1,
		font = buttonFont,
		)


	#stockPriceLabel1.insert(0, itemClicked.get())
	

	stockQuanityLabel1 = Entry(
		headerFrame1,
		width = 1,
		font = buttonFont,
		validate="all",
		validatecommand=Update_Total_Price
		)

	#validate="focusout", validatecommand=callback

	totalPriceLabel1 = Entry(
		headerFrame1,
		width = 1,
		font = buttonFont
		)
	
	stockNameLabel1.pack(side = LEFT, fill = X, anchor = CENTER, expand = 2.5)
	stockPriceLabel1.pack(side = LEFT, fill = X, anchor = CENTER, expand = 1.0)
	stockQuanityLabel1.pack(side = LEFT, fill = X, anchor = CENTER, expand = 1.0)
	totalPriceLabel1.pack(side = LEFT, fill = X, anchor = CENTER, expand = 1.5)


def Get_Item_Price(item):
	items = SelectItems()
	for i in items:
		if (item == i[0]):
			return i[1]

def Update_Price(Selection):
	global aItemName
	contentWidgets = overlayElementsContentFrame.winfo_children()
	rowEntries = list()
	for rowframe in contentWidgets:
		rowEntries.clear()
		for widget in rowframe.winfo_children():
			rowEntries.append(widget)
		
		print(rowEntries[0], Selection[0])
		rowEntries[1].delete(0, END)
		rowEntries[1].insert(0, Get_Item_Price(Selection[0]))
	aItemName = Selection[0]

def Update_Total_Price():
	print("Updating Total Price!")
	contentWidgets = overlayElementsContentFrame.winfo_children()
	rowEntries = list()
	rowCounter = 0



	for rowframe in contentWidgets:
		rowCounter += 1 
		rowEntries.clear()
		for widget in rowframe.winfo_children():
			rowEntries.append(widget)

		print(rowEntries[2].get())
		if rowEntries[2].get() == "":
			break

		if float(rowEntries[2].get().strip()) != 0:
			quanity = float(rowEntries[2].get().strip())
			print(quanity)
			pricePerQuanity = float(rowEntries[1].get())
			print(pricePerQuanity)
			rowEntries[3].delete(0, END)
			rowEntries[3].insert(0, quanity*pricePerQuanity)
			print("Current Row = " + str(rowCounter))

def Create_Entry_Row(masterFrame, stockName, stockPrice, stockQuanity, totalPrice, paddingX, paddingY):
	
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


#Does this work for multiple lines of code?
def Create_Entry_Row_Prefill(masterFrame, stockName, stockPrice, stockQuanity, totalPrice, paddingX, paddingY):
	
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
	
	stockNameLabel1.insert(0, stockName)
	stockPriceLabel1.insert(0, stockPrice)
	stockQuanityLabel1.insert(0, stockQuanity)
	totalPriceLabel1.insert(0, totalPrice)

	stockNameLabel1.pack(side = LEFT, fill = X, anchor = CENTER, expand = 2.5)
	stockPriceLabel1.pack(side = LEFT, fill = X, anchor = CENTER, expand = 1.0)
	stockQuanityLabel1.pack(side = LEFT, fill = X, anchor = CENTER, expand = 1.0)
	totalPriceLabel1.pack(side = LEFT, fill = X, anchor = CENTER, expand = 1.5)


	#print("Created a row of entries")

def Create_Entry_List(masterFrame, numberOfRows=6):
	for x in range(0, numberOfRows):
		Create_Entry_Row(masterFrame, x, "", x, "", 20, 10)

def Display_Entry_List(masterFrame, aListOfData):
	records = aListOfData
	totalTally = 0

	for row in records:
		Create_Entry_Row_Prefill(masterFrame, row[2], row[3], row[4], row[5], 20, 10)
		totalTally += row[5]

	headerFrame1 = Frame(
		masterFrame,
		width = 480,
		height = 10,
		borderwidth = 2,
		relief = "ridge"
		)
	headerFrame1.pack(fill = X)

	tempTitleLabel = Label(
		headerFrame1,
		text = "Total Sum: ",
		font = subHeadingFont
		)

	totalTallyLabel1 = Entry(
		headerFrame1,
		width = 10,
		font = buttonFont
		)

	totalTallyLabel1.insert(0, totalTally)

	totalTallyLabel1.pack(side = RIGHT)
	tempTitleLabel.pack(side = RIGHT)

def Create_Sales_Record_List(masterFrame, numberOfRows=6):
	for x in range(0, numberOfRows):
		Create_Sales_Record_Row(masterFrame, x, "", x, "", 20, 10)

def EditSalesRecord():
		
		sale_date = "2020-10-10"
		item_id = 3
		item_quantity = 3
		total_cost = 9.00
		sale_id = 1

		UpdateSalesRecord(sale_date, item_id, item_quantity, total_cost, sale_id)
		print("Edited a sales record")

def Populate_Sales_Report_Entries(listOfData=list()):
	
	headerWidgets = overlayElementsHeaderFrame.winfo_children() #Note this includes Frames
	contentWidgets = overlayElementsContentFrame.winfo_children() #Note this includes Frames

	c1 = 0
	c2 = 0
	for rowFrame in contentWidgets:
		for entry in rowFrame.winfo_children():
			if((entry.winfo_class() == 'Entry') and (c1 < len(listOfData))):
				entry.insert(0, listOfData[c1][c2])
				c2 += 1
			if (c2 >= 4):
				c1 += 1
				c2 = 0
		


def Create_List_Titles(master):
	'''
	No yet used as it failed to solve the problem, needs more time investment to fiddle with screen widths or text sizes

	zeroWidth = textHeaderFont.measure("0")
	#Header Frame
	labelWidth = (480/4)/zeroWidth
	#print(labelWidth)
	'''

	#Labels
	stockNameLabel = Label(
		master,
		text = "Stock Name",
		width = 13,
		font = textHeaderFont
		)
	stockPriceLabel = Label(
		master,
		text = "Price",
		width = 13,
		font = textHeaderFont
		)
	stockQuanityLabel = Label(
		master,
		text = "Quanity",
		width = 13,
		font = textHeaderFont
		)
	totalPriceLabel = Label(
		master,
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

	Create_List_Titles(overlayHeaderFrame)

	overlayElementsHeaderFrame = overlayHeaderFrame
	overlayElementsContentFrame = overlayContentFrame

	#Call to the function that selects and genegates the text entry boxes
	Create_Sales_Record_List(overlayContentFrame)

	stockOverlayFrame.pack()

def Display_Checkout_Overlay():
	global acceptState
	acceptState = 3
	

	global overlayElementsHeaderFrame
	global overlayElementsContentFrame
	Clear_Overlay()
	Unlock_Accept_Button()
	Unlock_Cancel_Button()

	CheckoutOverlayFrame = Frame(
		overlayFrame,
		width = 480,
		height = 600,
		borderwidth = 5,
		relief = "ridge"
		)

	overlayHeaderFrame = Frame(
		CheckoutOverlayFrame,
		width = 480
		)
	overlayHeaderFrame.pack(fill = X)

	overlayContentFrame = Frame(
		CheckoutOverlayFrame,
		width = 480
		)
	overlayContentFrame.pack(fill = X)

	#label in header content frame
	stockNameLabel = Label(
		overlayHeaderFrame,
		text = "Select a record to display",
		width = 20,
		font = textHeaderFont
		)
	stockNameLabel.pack_propagate(False)
	stockNameLabel.pack(side = BOTTOM, anchor = N)

	IDLabel = Label(
		overlayContentFrame,
		text = "ID",
		width = 1,
		font = textHeaderFont
		)
	
	dateStartLabel = Label(
		overlayContentFrame,
		text = "Start",
		width = 3,
		font = textHeaderFont
		)
	
	dateEndLabel = Label(
		overlayContentFrame,
		text = "End",
		width = 3,
		font = textHeaderFont
		)

	IDEntry = Entry(
		overlayContentFrame,
		width = 1,
		font = buttonFont
		)

	StartDateEntry = Entry(
		overlayContentFrame,
		width = 1,
		font = buttonFont
		)

	EndDateEntry = Entry(
		overlayContentFrame,
		width = 1,
		font = buttonFont
		)


	#spent too long making them side by side, just decided this works
	IDLabel.pack(side = TOP, anchor = W)
	IDEntry.pack(side = TOP, fill = X, anchor = E, expand = 2.5)
	dateStartLabel.pack(side = TOP, anchor = W)
	StartDateEntry.pack(side = TOP, fill = X, anchor = E, expand = 2.5)
	dateEndLabel.pack(side = TOP, anchor = W)
	EndDateEntry.pack(side = TOP, fill = X, anchor = E, expand = 2.5)


	overlayElementsHeaderFrame = overlayHeaderFrame
	overlayElementsContentFrame = overlayContentFrame

	CheckoutOverlayFrame.pack()

def Display_Sales_Record_Callback(DisplayVals):
	
	if(DisplayVals[1] == ''):
		DisplayVals[1] ='0000-00-00'
		
	if(DisplayVals[2] == ''):
		DisplayVals[2] ='2020-16-10'


	global overlayElementsHeaderFrame 
	global overlayElementsContentFrame
	global acceptState
	acceptState = 4

	Clear_Overlay()
	Lock_Sub_Buttons()
	Unlock_Accept_Button()
	Unlock_Cancel_Button()
	Unlock_Export_Button()
	Unlock_Edit_Button()

	#print("Displaying a sales record....")
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

	

	#Generate_Text_Entry(overlayHeaderFrame, "Date", CENTER, 5, (5, 5), 10)


	Create_Empty_Frame(overlayHeaderFrame, 50)

	Create_List_Titles(overlayHeaderFrame)

	#creates the rows which are then filled with entries
	#Create_Entry_List(overlayContentFrame)
	#Display_Entry_List(overlayContentFrame, LoadInData())
	overlayElementsHeaderFrame = overlayHeaderFrame
	overlayElementsContentFrame = overlayContentFrame
	#For Debugging Purposes

	'''
	DisplayVals has a list of three items (ID,StartDate,EndDate)

	This makes it work for just id, or dates
	there are also default values of '0000-00-00' and '2020-12-12' if the fields were supplied empty
	'''
	if(DisplayVals[0]==''):
		Display_Entry_List(overlayContentFrame, GetSalesRecord(DisplayVals[1], DisplayVals[2]))
	else:
		Display_Entry_List(overlayContentFrame, GetSalesRecord(DisplayVals[0]))

	#overlayElementsHeaderFrame = overlayHeaderFrame
	#overlayElementsContentFrame = overlayContentFrame

	#this function can be called without params to toggle state, or with the text 'lock' or 'unlock'
	#you will need to call 'unlock' before using a function like 'input' for example
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
	Title_Label_Creation("Sales Report Options")

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
	buttonFrame.pack_propagate(False)
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

def Draw_Sales_Report(date, period):
	global overlayElementsHeaderFrame 
	global overlayElementsContentFrame
	global acceptState
	global exportList
	global exportDate
	global exportPeriod

	acceptState = 6
	Lock_Sub_Buttons()
	#Unlock_Accept_Button()
	Unlock_Cancel_Button()
	Unlock_Export_Button()

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

	#logoLabel = Label(
	#	master = overlayHeaderFrame,
	#	image = phpLogo
	#	)
	#logoLabel.pack(side = LEFT, pady = (30,50))

	Generate_Text_Entry(overlayHeaderFrame, "Date", CENTER, 5, (5, 5), 10, date)
	Create_Empty_Frame(overlayHeaderFrame, 80)
	Create_List_Titles(overlayHeaderFrame)

	SalesReportData = GetSalesReport(date, period)
	numberOfEntries = len(SalesReportData)
	exportList = SalesReportData
	exportDate = date
	exportPeriod = period

	if (numberOfEntries > 10):
		numberOfEntries = 10
		
	Create_Entry_List(overlayContentFrame, numberOfEntries)

	overlayElementsHeaderFrame = overlayHeaderFrame
	overlayElementsContentFrame = overlayContentFrame

	Populate_Sales_Report_Entries(SalesReportData)

	stockOverlayFrame.pack()

def Accept_Button_Callback():
	global acceptState
	global aitemName
	#widgets = overlayElementsMasterFrame.winfo_children()
	
	headerWidgets = overlayElementsHeaderFrame.winfo_children() #Note this includes Frames
	contentWidgets = overlayElementsContentFrame.winfo_children() #Note this includes Frames
	
	Entries = list()
	
	
	if acceptState == 1:
		for widget in contentWidgets:
			if widget.winfo_class() == 'Entry':
				print(widget)
				Entries.append(widget.get())
		# call add item function
		print(Entries[0])
		print(Entries[1])

		InsertItem(Entries[0], Entries[1])
		Clear_Overlay()
		Lock_Sub_Buttons()

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
				print(tempList)
				addToSales(date, aItemName, tempList[1], tempList[2])
		print("Added Sales Record")
		Clear_Overlay()
		Lock_Sub_Buttons()

	elif acceptState == 3:
		print("Accept pressed from checkout screen")
		#possible loop to grap entry data
		LookupVals = list()
		for widget in contentWidgets:
			if(widget.winfo_class() == "Entry"):
				LookupVals.append(widget.get())
		
		print(LookupVals)

		Clear_Overlay()
		Lock_Sub_Buttons()
		Display_Sales_Record_Callback(LookupVals)
		
	elif acceptState == 4:
		print("Displaying a Sales Record")
		EditSalesRecord()
		Clear_Overlay()
		Lock_Sub_Buttons()
		
	elif acceptState == 5:
		for widget in headerWidgets:
			if(widget.winfo_class() == 'Entry'):
				date = widget.get()

		Clear_Overlay()
		Lock_Sub_Buttons()
		Draw_Sales_Report(date, reportOptionButtonState)



def Cancel_Button_Callback():
	print("I Canceled Something")
	Clear_Overlay()
	Lock_Sub_Buttons()
	

def Edit_Button_Callback():
	print("I pressed edit")
	Clear_Overlay()
	Lock_Sub_Buttons()
	Change_Entry_State('unlock')#this is all thats needed internally to unlock all the entry fields

def Export_Button_Callback():
	print("I Exported Something")
	Clear_Overlay()
	Lock_Sub_Buttons()

	exportCSV(exportList, exportDate, exportPeriod)



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
		#image = phpLogo
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

	#Display Sales Record Button
	displaySalesRecordButton = Button(
		master=mainMenuButtonsFrame,
		text = "Display/Edit \na Sales Record",
		width = 20,
		height = 3,
		font = buttonFont,
		bg = LIGHTGRAY,
		fg = ALMOSTBLACK,
		command = Display_Checkout_Overlay#Display_Sales_Record_Callback
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
	EditButton  = Button(
		master = subMenuFrame,
		text = "Edit",
		width = 20,
		height = 3,
		font = buttonFont,
		bg = LIGHTGRAY,
		fg = ALMOSTBLACK,
		state = DISABLED,
		command = Edit_Button_Callback
		)
	EditButton.pack(side = LEFT,anchor = E)

#Constants
LIGHTERGRAY = "#cccccc"
LIGHTGRAY = "#a6a6a6"
ALMOSTBLACK = "#292929"

#Global Varaibles
root = Tk()
root.geometry('1280x960')
#phpLogo = PhotoImage(file="images/logo2.png")
#overlayFrameList = [] No used anymore, Delete if no use is found
overlayListElements = [4]
print(overlayListElements)
acceptState = 0
reportOptionButtonState = bool

#Overlay Elements Master Frame Reference
overlayElementsHeaderFrame = Frame()
overlayElementsContentFrame = Frame()
itemClicked = StringVar()

#itemClicked.trace('w', Update_Price)

#Global variable for record data to be exported
exportList = list()
exportDate = 0
exportPeriod = 0

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