import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database = "db_name"
)

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



foundRecords = GetSalesRecord("yess", "no", "4")

for row in foundRecords:
    print("Sale ID: " + str(row[0]))
    print("Sale Date: " + str(row[1]))
    print("Item Name: " + str(row[2]))
    print("Quantity: " + str(row[3]))
    print("Total Cost: " + str(row[4]))
    print("")







