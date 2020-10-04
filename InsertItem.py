import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sreps"
)
print(mydb)

mycursor = mydb.cursor()

def InsertItem (itemName, itemPrice):
    if (itemName == "") or (itemPrice == ""):
        print("Error, an item must have a Name and Price")
    else:
        query = "INSERT INTO items(item_name, item_price) VALUES ('" + itemName + "', '" + itemPrice + "')"
        mycursor.execute(query)
        mydb.commit()
        print(mycursor.rowcount, "record inserted")
