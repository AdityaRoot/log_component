from log_component import LogComponent
import unittest
import time
import datetime

class TestLogComponent(unittest.TestCase):

    def setUp(self):
        self.log = LogComponent()

    def tearDown(self):
        self.log.stop(wait=True)
        # Delete the log file
        # filename = self.log.current_file.name
        # import os
        # os.remove(filename)

    def test_write(self):
        self.log.write("Test Write\n")


        # Assert that file exists, and has the correct content
        filename = self.log.current_file.name
        with open(filename) as f:
            content = f.read()
            self.assertIn( "Test Write\n",content )


    def test_check_cross_midnight(self):
        # Set current date to yesterday
        self.log.check_cross_midnight()
        self.assertIsNotNone(self.log.current_date)
        
        self.log.current_date = datetime.datetime.now().date() - datetime.timedelta(days=1)

        # Check that midnight has passed
        message = "Midnight Passed\n"
        self.log.write(message)

        # Assert that a new file was created, with the correct content
        filename = self.log.current_file.name
        self.assertEqual(filename, datetime.datetime.now().strftime("%Y-%m-%d.log"))
        
    def test_stop(self):
        # Stop the component
        self.log.stop(wait=True)

        # Assert that the file is closed
        self.assertIsNone(self.log.current_file)

    def test_stop_async(self):
        # Stop the component
        self.log.stop(wait=False)
        # Assert that the file is closed
        self.assertIsNone(self.log.current_file)

    def test_handle_error(self):
        message = None
        with self.assertRaises(Exception):
            self.log.write(message)


if __name__ == "__main__":
    unittest.main()


            
    
