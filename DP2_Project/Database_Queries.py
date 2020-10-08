import mysql.connector

def cursorReset():
    cursor = mydb.cursor()

def printSales():
    cursor.execute ('SELECT * FROM Sales')
    records = cursor.fetchall()

    if not records:
        print("The records are currently empty.")
    else:
        for row in records:
            print("ID: " + str(row[0]))
            print("Date: " + str(row[1]))
            print("Item ID: " + str(row[2]))
            print("Quantity: " + str(row[3]))
            print("Cost: " + str(row[4]))
    cursorReset()

def InsertItem (itemName, itemPrice):
    if (itemName == "") or (itemPrice == ""):
        print("Error, an item must have a Name and Price")
    else:
        query = "INSERT INTO items(item_name, item_price) VALUES ('" + itemName + "', '" + itemPrice + "')"
        mycursor.execute(query)
        mydb.commit()
        print(mycursor.rowcount, "record inserted")

#Can't be using Inputs, all data should be passed through variables
def addToSales(aSalesDate, aItemID, aItemQuant, aTotalCost):
    sale_date = aSalesDate
    item_id = aItemID
    item_quantity = aItemQuant
    total_cost = aTotalCost

    sql = "INSERT INTO Sales (sale_date, item_id, item_quantity, total_cost) VALUES (%s, %s, %s, %s)"
    val = (sale_date, item_id, item_quantity, total_cost)
    mycursor.execute (sql, val)

def GetSalesRecord(startDate = "", endDate = "", saleID = ""):
    query = ""

    if (saleID != ""):
        query = "SELECT Sales.sale_id, Sales.sale_date, Items.item_name, Sales.item_quantity, Sales.total_cost FROM Sales INNER JOIN Items ON Sales.item_id = Items.item_id WHERE Sales.sale_id = " + saleID
    elif (startDate != "") and (endDate == ""):
        query = "SELECT Sales.sale_id, Sales.sale_date, Items.item_name, Sales.item_quantity, Sales.total_cost FROM Sales INNER JOIN Items ON Sales.item_id = Items.item_id WHERE Sales.sale_date >= '" + startDate + "'"
    elif (startDate != "") and (endDate != ""):
        query = "SELECT Sales.sale_id, Sales.sale_date, Items.item_name, Sales.item_quantity, Sales.total_cost FROM Sales INNER JOIN Items ON Sales.item_id = Items.item_id WHERE Sales.sale_date BETWEEN '" + startDate + "' AND '" + endDate + "'"
    else:
        print("Error, invalid search parameters.")
        return -1

    mycursor = mydb.cursor()
    mycursor.execute(query)
    records = mycursor.fetchall()

    return records

#We can't use inputs as it is meant to be going through the GUI
def editSales(aFieldIndex, aRecord, aValue):
    FieldIndex = aFieldIndex
    Record = aRecord
    Value = aValue
    
    print('Select a field to edit: ')
    cursor.execute ('desc Sales')
    temp = mycursor.fetchall()
    for row in temp:
        print(row[0])

    inputValid = False
    while (inputValid == False):

        Field = input()
        if Field.lower() in str(temp):
            inputValid = True
        else:
            print("Not a field.")

    Field = input()

    cursorReset()

    print('Select which record to edit: ')
    sql = ("SELECT " + Field + " FROM Sales")
    mycursor.execute (sql)
    temp = cursor.fetchall()
    for row in temp:
        print(row[0])
    inputValid = False
    while (inputValid == False):

        Record = input()
        if Record.lower() in str(temp):
            inputValid = True
        else:
            print("Not a record.")
    
    Record = input()

    cursorReset()

    Value = input('Write the value you want to replace it with: ')
    sql = ("UPDATE Sales SET " + Field + " = '" + Value + "' WHERE " + Field + " = '" + Record + "'")
    mycursor.execute (sql)

def SelectItemNames():
    itemNameList = []
    mycursor.execute("SELECT item_name FROM items")
    for x in mycursor:
        itemNameList.append(x)
    return itemNameList

def SelectItemPrices():
    itemPriceList = []
    mycursor.execute("SELECT item_price FROM items")
    for x in mycursor:
        itemPriceList.append(x)
    return itemPriceList

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sreps"
)
print(mydb)
mycursor = mydb.cursor()