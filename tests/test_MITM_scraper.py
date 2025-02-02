import unittest

from src.MITM_scraper import get_response, clean_salary

class MITM_scraper_tests(unittest.TestCase):
    def test_expirience(self):
        response = get_response()
        self.assertEqual(type(response), list)
        self.assertEqual(type(response[0]), dict)
        self.assertTrue("title" in response[0])

class clean_salary_tests(unittest.TestCase):
    def test_expirience(self):
        self.assertEqual(clean_salary('$Depend on Exp'), [-1])
        self.assertEqual(clean_salary('Depends on Experience'), [-1])
        self.assertEqual(clean_salary('$DOE'), [-1])

    def test_no_salary(self):
        self.assertEqual(clean_salary('-'), [-2])
        self.assertEqual(clean_salary('$0 - $0'), [-2])
        self.assertEqual(clean_salary('0'), [-2])

    def test_numbers(self):
        self.assertEqual(clean_salary('$125,000 - $130,000 annually'), [125000, 130000])
        self.assertEqual(clean_salary('$60 - $70 hourly'), [120000, 140000])
        self.assertEqual(clean_salary('USD 140,000.00 - 160,000.00 per year'), [140000, 160000])
        self.assertEqual(clean_salary('USD 70.00 - 86.00 per hour'), [140000, 172000])
        self.assertEqual(clean_salary('USD 70 per hour'), [140000])
        self.assertEqual(clean_salary('USD 70.00 per hour'), [140000])
        self.assertEqual(clean_salary('USD 125,000'), [125000])
       
if __name__ == '__main__':
    unittest.main() 
    