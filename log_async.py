# Imports
import asyncio
import datetime
import nest_asyncio
nest_asyncio.apply()


class LogComponent:
    def __init__(self):
        # Initialize variables
        self.current_file = None
        self.current_date = None
        self.lock = asyncio.Lock() # Lock to prevent multiple tasks from writing to the same file at the same time
        self.loop = asyncio.get_event_loop() # Get the event loop

    async def write(self, message):
        self.check_cross_midnight() # Check if the date has changed
        await self._write_to_file(message) # Write to the file

    async def check_cross_midnight(self):
        current_date = datetime.datetime.now().date()

        if self.current_date != current_date:
            self.current_date = current_date
            self._create_new_file()

    async def _create_new_file(self):
        # Close the current file
        if self.current_file:
            self.current_file.close()
            self.current_file = None

        # Create a new file
        filename = datetime.datetime.now().strftime("%Y-%m-%d.log")
        self.current_file = open(filename, "a")

    async def _write_to_file(self, message):
        # Acquire lock
        await self.lock.acquire()
        try:
            self.current_file.write(message)
        except Exception as e:
            self._handle_error(e)
        finally:
            self.lock.release()


    def stop(self, wait=False):
        if wait:
            # pending = asyncio.all_tasks(self.loop)
            # self.loop.run_until_complete(asyncio.gather(*pending))
            self.loop.run_until_complete(self._stop())
        else:
            self.loop.create_task(self._stop())

    async def _stop(self):
        if self.current_file:
            self.current_file.close()
            self.current_file = None

    def _handle_error(self, error):
        print(f"Error occurred: {error}")

    
