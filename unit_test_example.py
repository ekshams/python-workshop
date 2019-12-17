# unit test example

import unittest
import sum
class SampleTestCase(unittest.TestCase):
    def test_sum_success(self):
        res = sum.calculate_sum(3, 3)
        self.assertEqual(res, 6)
        
    def test_sum_should_not_6(self):
        res = sum.calculate_sum(3, 2)
        self.assertNotEqual(res,6)
        
class StringTestCase(unittest.TestCase):
    def test_string_shold_capital(self):
        res = sum.convert_to_upper_case("hey")
        self.assertEqual(res, "hey".upper())
        
    def test_string_shold_capital1(self):
        res = sum.convert_to_upper_case("HEY")
        self.assertEqual(res, "HEY".upper())
        
# Test suite

def suite():
    suite = unittest.TestSuite()
    suite.addTest(SampleTestCase('test_sum_success'))
    suite.addTest(StringTestCase('test_string_shold_capital'))
    return suite
        
if __name__ == "__main__":
    # unittest.main()
    runner = unittest.TextTestRunner()
    runner.run(suite())