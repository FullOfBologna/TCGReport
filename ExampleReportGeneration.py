from pdfquery import PDFQuery
import pandas as pd
import csv
import sys

from InventoryParser import InventoryParser

def main():

    args = sys.argv[1:]

    filename = args[0]

    invReport = InventoryParser(filename)

    fields = invReport.get_Fields()
    totalMarket = invReport.get_totalValueMarket()
    totalListed = invReport.get_totalValueListed()
    totalLow = invReport.get_totalValueLow()

    print(f"Market Value: ${totalMarket}")
    print(f"Listed:       ${totalListed}")
    print(f"Low Price:    ${totalLow}")

    # print(fields)

if __name__ == '__main__':
    main()