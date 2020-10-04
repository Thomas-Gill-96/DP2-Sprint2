# imports
import pyodbc
import mysql.connector

# constants

# variables
running = True

# SQL stuff
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sreps"
)

cursor = mydb.cursor()

# Methods
def printAll():
    cursorReset()

    printItems()
    printSales()

def printItems():
    cursor.execute ('SELECT * FROM Items')
    records = cursor.fetchall()

    if not records:
        print("The records are currently empty.")
    else:
        for row in records:
            print("ID: " + str(row[0]))
            print("Name: " + str(row[1]))
            print("Price: " + str(row[2]))
    cursorReset()

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

def addToSales(aSalesDate, aItemID, aItemQuant, aTotalCost):
    sale_date = aSalesDate
    item_id = aItemID
    item_quantity = aItemQuant
    total_cost = aTotalCost

    sale_date = input("Enter the sales date: ")
    item_id = input("Enter the item's id: ")
    item_quantity = input("Enter the number of items sold: ")
    total_cost = input("Enter the total cost: ")

    sql = "INSERT INTO Sales (sale_date, item_id, item_quantity, total_cost) VALUES (%s, %s, %s, %s)"
    val = (sale_date, item_id, item_quantity, total_cost)
    cursor.execute (sql, val)

def editSales(aFieldIndex, aRecord, aValue):
    FieldIndex = aFieldIndex
    Record = aRecord
    Value = aValue
    
    print('Select a field to edit: ')
    cursor.execute ('desc Sales')
    temp = cursor.fetchall()
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
    cursor.execute (sql)
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
    cursor.execute (sql)

def cursorReset():
    cursor = mydb.cursor()


while running:
    cursorReset()
    # For debugging purposes.
    print('This is the database as it is')
    printAll()

    #The arguments down below are just dummy variables. Replace them with actual arguments from GUI inputs.
    while(False):
        addToSales(aSalesDate, aItemID, aItemQuant, aTotalCost)
        editSales(aFieldIndex, aRecord, aValue)
        break

    while(True):
        mydb.commit()
        break

    print(cursor.rowcount, "record(s) affected")
    printAll()
    running = False



#print('-- The End --')