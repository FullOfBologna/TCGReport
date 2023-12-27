from pdfquery import PDFQuery
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

    now = datetime.datetime.now()
    nowString = now.strftime("%Y-%m-%d")    
    
    reportString = "\n"
    reportString += "Storefront Inventory Report\n"
    reportString += nowString + "\n"
    reportString += "\n"
    reportString += "==============================\n"
    reportString += f"Listed Card Value\n"
    reportString += f"=============================\n"
    reportString += f"Market Value: ${totalMarket}\n"
    reportString += f"Listed:       ${totalListed}\n"
    reportString += f"Low Price:    ${totalLow}\n"

    outputReportName = "InventoryPriceReport_" + nowString + ".txt"

    print(reportString)

    

    # print(fields)

if __name__ == '__main__':
    main()