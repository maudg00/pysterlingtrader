import time
from time import sleep
import unittest

from regex import A
from connector import ConnectorSterling, ConnectorSymbolData
account = "DMSTPU0008275"
symbol="AAPL"
class TestStringMethods(unittest.TestCase):

    def test_get_open_price(self):
        print("\n")
        aaplSymbol = ConnectorSymbolData("AAPL", account=account, market="")
        initPrice=aaplSymbol.get_open_price()
        print("Open",initPrice)
        self.assertTrue(initPrice>0)
    
    def test_get_close_price(self):
        print("\n")
        aaplSymbol = ConnectorSymbolData("AAPL", account=account, market="")
        initPrice=aaplSymbol.get_close_price()
        print("Close",initPrice)
        self.assertTrue(initPrice>0)

    def test_get_bid_price(self):
        print("\n")
        aaplSymbol = ConnectorSymbolData("AAPL", account=account, market="")
        initPrice=aaplSymbol.get_bid_price()
        print("Bid",initPrice)
        self.assertTrue(initPrice>0)
    
    def test_get_ask_price(self):
        print("\n")
        aaplSymbol = ConnectorSymbolData("AAPL", account=account, market="")
        initPrice=aaplSymbol.get_ask_price()
        print("Ask",initPrice)
        self.assertTrue(initPrice>0)
    
    def test_get_last_price(self):
        print("\n")
        aaplSymbol = ConnectorSymbolData("AAPL", account=account, market="")
        initPrice=aaplSymbol.get_last_price()
        print("Last",initPrice)
        self.assertTrue(initPrice>0)
    
    def test_get_cum_vol(self):
        print("\n")
        aaplSymbol = ConnectorSymbolData("AAPL", account=account, market="")
        initVol=aaplSymbol.get_cum_vol()
        print("CumVol:",initVol)
        self.assertTrue(initVol>0)

    def test_get_avg_vol(self):
        print("\n")
        aaplSymbol = ConnectorSymbolData("AAPL", account=account, market="")
        initVol=aaplSymbol.get_avg_vol()
        print("AvgVol:",initVol)
        self.assertTrue(initVol>0)
    

if __name__ == '__main__':
    
    unittest.main()