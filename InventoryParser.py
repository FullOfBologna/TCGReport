import pandas as pd

##
# Class InventoryParser: 
#   Read in the exported csv from tcg player live inventory.
#   Parse the data into various relevant statistics for use in a higher level script. 
#   genReport is the immediate entry point. 
#
#

def class InventoryParser:
    def __init__(self, filename)
        self.filename = filename
        self.totalValueListed = 0
        self.totalValueMarket = 0
        self.avgValue = 0
        self.productsCount = None
        self.invDF = None
        self.ProductNames = None
        self.fileDate=''

        genReport()

    def genReport(self):
        if self.filename == None:
            return "Error: Unable to open File."

        df = pd.read_csv(filename)

        self.invDF = df[df["Total Quantity"]>0 in df]

    def get_totalValueMarket(self):
        return self.totalValueMarket
    
    def get_totalValueMarket(self):
        return self.totalValueMarket
    
    def get_ProductNames(self):
        return self.ProductNames
    
    def get_invDF(self):
        return self.invDF
    
    def get_avgValue(self):
        return self.avgValue
    