from log_async import LogComponent
import asyncio
import unittest
import datetime
import time

class TestLogComponent(unittest.TestCase):

    def setUp(self):
        self.log = LogComponent()

    def tearDown(self):
        self.log.stop(wait=True)

    def test_write(self):
        self.log.write("Hello")
        self.log.write("World")
        self.log.write("!")
        
        filename = datetime.datetime.now().strftime("%Y-%m-%d.log")
        with open(filename) as f:
            content = f.read()
            self.assertEqual(content, "HelloWorld!")
        
    # def test_check_cross_midnight(self):
    #     self.log.current_date = datetime.datetime(2020, 1, 1).date()
    #     self.log.check_cross_midnight()
    #     self.assertEqual(self.log.current_date, datetime.datetime.now().date())


    def test_new_file_on_midnight(self):
        self.log.current_date = datetime.datetime(2020, 1, 1).date()
        self.log.check_cross_midnight()
        self.assertEqual(self.log.current_date, datetime.datetime.now().date())

    def test_stop(self):
        self.log.stop(wait=True)
        self.assertIsNone(self.log.current_file)
        
    def test_stop_without_wait(self):
        self.log.stop(wait=False)
        self.assertIsNone(self.log.current_file)
        

if __name__ == "__main__":
    unittest.main()

