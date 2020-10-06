import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sreps"
)
print(mydb)

mycursor = mydb.cursor()

def SelectItem (itemName, itemPrice):
    itemNameList = []
    itemPriceList = []
    mycursor.execute("SELECT item_name FROM items")
    for x in mycursor:
        itemNameList.append(x)
    mycursor.execute("SELECT item_price FROM items")
    for x in mycursor:
        itemPriceList.append(x)

