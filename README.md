# log_component

I implemented one set without asyncio, as I have never done async programming before, I wanted to try programming it via threads before trying to implement it via asyncio.

I still had some errors/bugs while using asyncio that I have not been able to figure out in the allotted time, and would need to go deeper into the asyncio documentation to understand the backend and how to robustly implement the system.

# Design
The design of the algorithm is rather rudimentary, with a simple date and file variable keeping track of the current date and filename. It is possible to forgo one of the variables however I believe splitting them leads to cleaner, easier to maintain code.

After that, the majority of the functions are short and self explanatory.
