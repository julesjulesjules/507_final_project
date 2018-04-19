### unit testing
import unittest
from main_program import *

#class TestScrapes(unittest.TestCase):

#    def test_UOscrape(self):


class TestAnthroProcess(unittest.TestCase):

    def test_ri(self):
        td = {"one": 1, "two": 2}
        output = read_in_ANTfiles()
        self.assertEqual(type(td), type(output))

    def test_structure(self):
        td = {"one": 1, "two": 2}
        tt = ("one", 1)
        tl = ["one", 1, 2]
        output = read_in_ANTfiles()
        struc = match_anthros(output)
        self.assertEqual(type(struc), type(td))
        for each in struc:
            self.assertEqual(type(struc[each]), type(tl))
        for each in struc:
            self.assertEqual(type(struc[each][0]), type(tt))
            #also need to test that items in list are tuples

#class TestDatabase(unittest.TestCase):

#    def test_bar_table(self):


#class TestSQLRequests(unittest.TestCase):

#    def test_pattern(self):
#        conn = sqlite3.connect("storeitem.db")
#        cur = conn.cursor()
#        floral = '''select Brand.Name, ItemName, ListPrice FROM Items JOIN
#                    Brand ON Brand.Id=Items.BrandId
#                    WHERE Items.GenderId=2
#                    AND ItemName LIKE "%floral%" LIMIT 10'''

if __name__ == '__main__':
    unittest.main()
