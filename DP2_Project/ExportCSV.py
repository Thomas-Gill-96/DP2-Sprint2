import csv

def exportCSV(exportList, exportDate, exportPeriod):
    with open('salesReport.csv', 'w', newline='') as myfile:
        writer = csv.writer(myfile)
        firstLine = ""
        if exportPeriod == False:
            firstLine = "Sales Records for WEEK of " + exportDate
        else:
            firstLine = "Sales Records for MONTH of " + exportDate

        writer.writerow([str(firstLine)])
        secondLine = {"Item name", "Item price", "Quantity", "Total price"}
        writer.writerow(secondLine)
        writer.writerows(exportList)
        myfile.close() 