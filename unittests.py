import unittest
import login

class TestMyStuff(unittest.TestCase):
    #write our test cases
    #assert means we are assuming something to be true
    #below testcases are for login validation
    def test_1(self):
        self.assertEqual(True,login.loginvalidationreturn('mukul','mukul123'))
    def test_2(self):
        self.assertEqual(False,login.loginvalidationreturn('ewgew','mukul123'))
    def test_3(self):
        self.assertEqual(True,login.loginvalidationreturn('omkar','omkar123'))
    #the below test cases are for dictionary word checking(whether they are present in json or not)    
    def test_4(self):
        self.assertEqual(False,login.check_wrd("esewvgewvwvgew"))
    def test_5(self):
        self.assertEqual(True,login.check_wrd("rain"))
    def test_6(self):
        self.assertEqual(True,login.check_wrd("qwe"))
    def test_7(self):
        self.assertEqual(False,login.check_wrd("4"))
    




def main():
    suite=unittest.TestLoader().loadTestsFromTestCase(TestMyStuff)
    
    unittest.TextTestRunner(verbosity=3).run(suite)
main()