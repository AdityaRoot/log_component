# Imports
import datetime
import threading

class LogComponent:
    def __init__(self):
        # Initialize variables
        self.current_file = None
        self.current_date = None
        self.lock = threading.Lock() # Lock to prevent multiple threads from writing to the same file at the same time

    def write(self, message):
        self.check_cross_midnight() # Check if the date has changed
        self._write_to_file(message) # Write to the file

    def check_cross_midnight(self):
        current_date = datetime.datetime.now().date()
        # Check if the date has changed
        if self.current_date != current_date:
            self.current_date = current_date
            self._create_new_file()

    def _create_new_file(self):
        # Close the current file
        if self.current_file:
            self.current_file.close()
            self.current_file = None
        # Create a new file
        filename = datetime.datetime.now().strftime("%Y-%m-%d.log")
        self.current_file = open(filename, "a")

    def _write_to_file(self, message):
        # Acquire the lock
        self.lock.acquire()
        try:
            self.current_file.write(message)
        finally:
            self.lock.release()


    def stop(self, wait=False):
        # Close the current file
        if wait:
            self.lock.acquire()
            try:
                if self.current_file:
                    self.current_file.close()
                    self.current_file = None
            finally:
                self.lock.release()
        else:
            if self.current_file:
                self.current_file.close()
                self.current_file = None

    # Error handling
    def _handle_error(self, error):
        print(f"Error occurred: {error}")

    
        
