import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database = "db_name"
)


def GetSalesReport(inputDate = "", period = False):
    query = ""
    if (inputDate != ""):
        if (period == False):
            query = "SELECT item_name, SUM(item_quantity) AS total_quantity, SUM(total_cost) AS total_cost FROM sales INNER JOIN  items ON sales.item_id = items.item_id WHERE WEEK(sale_date,1) = WEEK('" + inputDate + "',1) GROUP BY sales.item_id ORDER BY total_cost DESC;"
        else:
            query = "" # TO DO
    else:
        print("Error, date required.")
        return -1

    mycursor = mydb.cursor()
    mycursor.execute(query)
    records = mycursor.fetchall()

    return records

salesReports = GetSalesReport("2020-09-23", False)

for row in salesReports:
    print("Item Name: " + str(row[0]))
    print("Total Quantity: " + str(row[1]))
    print("Total Cost: " + str(row[2]))
    print("")
