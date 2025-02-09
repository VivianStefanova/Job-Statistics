import unittest

import src.MITM_scraper as mi
import src.API_scraper as api

class MITM_scraper_tests(unittest.TestCase):
    def test_expirience(self):
        response = mi.get_response()
        self.assertEqual(type(response), list)
        self.assertEqual(type(response[0]), dict)
        self.assertTrue("title" in response[0])

class MITM_clean_salary_tests(unittest.TestCase):
    def test_expirience(self):
        self.assertEqual(mi.clean_salary('$Depend on Exp'), [-1])
        self.assertEqual(mi.clean_salary('Depends on Experience'), [-1])
        self.assertEqual(mi.clean_salary('$DOE'), [-1])

    def test_no_salary(self):
        self.assertEqual(mi.clean_salary('-'), [-2])
        self.assertEqual(mi.clean_salary('$0 - $0'), [-2])
        self.assertEqual(mi.clean_salary('0'), [-2])

    def test_numbers(self):
        self.assertEqual(mi.clean_salary('$125,000 - $130,000 annually'), [125000, 130000])
        self.assertEqual(mi.clean_salary('$60 - $70 hourly'), [120000, 140000])
        self.assertEqual(mi.clean_salary('USD 140,000.00 - 160,000.00 per year'), [140000, 160000])
        self.assertEqual(mi.clean_salary('USD 70.00 - 86.00 per hour'), [140000, 172000])
        self.assertEqual(mi.clean_salary('USD 70 per hour'), [140000])
        self.assertEqual(mi.clean_salary('USD 70.00 per hour'), [140000])
        self.assertEqual(mi.clean_salary('USD 125,000'), [125000])
       
class API_scraper_tests(unittest.TestCase):
    def test_expirience(self):
        response = api.get_response()
        self.assertEqual(type(response), list)
        self.assertEqual(type(response[0]), dict)
        self.assertTrue("title" in response[0])
        self.assertTrue("salary_min" in response[0])
        self.assertTrue("salary_max" in response[0])

class API_clean_salary_tests(unittest.TestCase):
    def test_numbers(self):
        self.assertEqual(api.clean_salary('8500.07'), 8500) 
        self.assertEqual(api.clean_salary("2222"), 2222)
        self.assertEqual(api.clean_salary('3434.47'), 3434)
              
if __name__ == '__main__':
    unittest.main() 
    