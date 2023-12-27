from pdfquery import PDFQuery
import pandas as pd
import csv
import sys

import InventoryParser from InventoryParser

def main():

    args = sys.argv[1:]

    filename = args[0]

    InventoryParser invReport(filename)

if __name__ == 'main':
    main()