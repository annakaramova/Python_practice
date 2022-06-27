import unittest
from MainPage import MainPage


class AutomationRemarks(unittest.TestCase):
    def setUp(self):
        self.main_page = MainPage()

    def tearDown(self):
        self.main_page.close()

    def test_main_page(self):
        self.assertEqual(self.main_page.get_remarks().text, "Automation Remarks")


if __name__ == "__main__":
    unittest.main()
