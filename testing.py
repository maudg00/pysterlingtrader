import time
from time import sleep
import unittest

from regex import A
from connector import ConnectorSterling, ConnectorSymbolData
account = "DMSTPU0008275"
symbol="AAPL"
class TestStringMethods(unittest.TestCase):

    def test_get_open_price(self):
        aaplSymbol = ConnectorSymbolData("AAPL", account=account, market="")
        initPrice=aaplSymbol.get_last_price()
        print(initPrice)
        symbol = 'AAPL'
        price = 5
        con = ConnectorSterling(verbose=False)

        ordId, status = con.send_limit(account, symbol, 100, price, "ARCA", "B")

        if status == 0:
            print(f'Cancel order {ordId}')
            time.sleep(1)
            con.cancel_order_id(account, ordId)
            time.sleep(1)
            status = con.order_status(ordId + 'cancel')
            print(f'Now order in status {status}')
        else:
            print(f"Order status: {status}")

        positions = con.get_all_account_positions(account)

        print('\n'.join([str(x) for x in positions]))

        for p in positions:
            symb_position = con.get_open_shares(account, p.symbol)
            print(f'{p.symbol} open shares is {symb_position}')
        
        while(1):

            price=aaplSymbol.get_last_price()
            if price!=initPrice:
                print(price)
                break
        self.assertTrue(price>0)
    '''
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    '''

if __name__ == '__main__':
    
    unittest.main()