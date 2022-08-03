import unittest
from connector import ConnectorSterling
account = ""
symbol="SPY"
class TestStringMethods(unittest.TestCase):

    def test_get_last_price(self):
        con = ConnectorSterling(verbose=False)
        self.assertTrue(con.get_last_price(symbol)>0)
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