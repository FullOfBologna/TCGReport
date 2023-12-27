# from pdfquery import PDFQuery
import pandas as pd
import csv
import sys
import datetime

from InventoryParser import InventoryParser

def main():

    args = sys.argv[1:]

    filename = args[0]

    invReport = InventoryParser(filename)

    fields = invReport.get_Fields()
    totalMarket = invReport.get_totalValueMarket()
    totalListed = invReport.get_totalValueListed()
    totalLow = invReport.get_totalValueLow()
    totalCards = invReport.get_totalCards()
    avgPerCard = invReport.get_avgValuePerCard()


    now = datetime.datetime.now()
    nowString = now.strftime("%Y-%m-%d")    
    
    reportString = "\n"
    reportString += "Storefront Inventory Report\n"
    reportString += nowString + "\n"
    reportString += "\n"
    reportString += f"Total Cards Listed: {totalCards}"
    reportString += "\n"
    reportString += "==============================\n"
    reportString += f"Listed Card Value\n"
    reportString += f"=============================\n"
    reportString += f"Market Value: ${totalMarket}\n"
    reportString += f"Listed:       ${totalListed}\n"
    reportString += f"Low Price:    ${totalLow}\n"
    reportString += "\n"
    reportString += f"Average Value Per Card: {avgPerCard}\n"


    outputReportName = "Reports/InventoryPriceReport_" + nowString + ".txt"

    # print(reportString)

    with open(outputReportName,'w') as outputFile: 
        outputFile.write(reportString)
    


    # print(fields)

if __name__ == '__main__':
    main()