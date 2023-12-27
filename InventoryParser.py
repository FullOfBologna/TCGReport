import pandas as pd

##
# Class InventoryParser: 
#   Read in the exported csv from tcg player live inventory.
#   Parse the data into various relevant statistics for use in a higher level script. 
#   genReport is the immediate entry point. 
#
#

class InventoryParser:
    def __init__(self, filename):
        self.filename = filename
        self.totalValueListed = 0
        self.totalValueMarket = 0
        self.avgValue = 0
        self.productsCount = None
        self.invDF = None
        self.ProductNames = None
        self.fileDate=''

        self.genReport()

    def genReport(self):
        if self.filename == None:
            return "Error: Unable to open File."

        df = pd.read_csv(self.filename)

        self.invDF = df[df["Total Quantity"] > 0]

        self.totalValueMarket = self.invDF["TCG Market Price"].mul(self.invDF["Total Quantity"]).sum()
        self.totalValueListed = self.invDF["TCG Marketplace Price"].mul(self.invDF["Total Quantity"]).sum()
        self.totalValueLow = self.invDF["TCG Low Price"].mul(self.invDF["Total Quantity"]).sum()
        
        # self.total
    def get_Fields(self):
        self.columnNames = list(self.invDF.columns)
        return self.columnNames
    
    def get_totalValueMarket(self):
        return self.totalValueMarket
    
    def get_totalValueListed(self):
        return self.totalValueListed
    
    def get_totalValueLow(self):
        return self.totalValueLow
    
    def get_ProductNames(self):
        return self.ProductNames
    
    def get_invDF(self):
        return self.invDF
    
    def get_avgValue(self):
        return self.avgValue
    
    def reportPrettyPrint(self):
        outStr = "Under Construction"
        print(outStr)
        