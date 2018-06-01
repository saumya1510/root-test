Problem statement:
https://gist.github.com/dan-manges/1e1854d0704cb9132b74

To run this program, enter "python rootCodingTest.py <filename>" in your terminal. A sample file has been provided called "input".
To run the tests, enter "python -m unittest tester"

Approach Overview:
My program reads the file which contains the required input. It stores the driver and trip details in a Python Dictionary object. The dictionary would be of the form:
	{driver name: (total distance, total time)}
The values of distance and time would be updated while reading the input. Here, if the speed for that trip (distance/time) is not between 5 and 100, it won't be added to the dictionary. Once the entire file is read and parsed, the program calculates average speed for all drivers and prints the speed and the distance to an output file. 


Assumptions:
The program is made to be fault tolerant. However, some assumptions are made, as follows:
1. The driver names would be unique.
2. Average Speed = total distance/total time


Approach in Detail:

1. Built-in objects
If required, it would have been possible to create a class for the drivers and add the methods for sorting, and updating the values to that class. That would have been the ideal way of solving this problem, if there was a scope for reusability of the objects or expansion of the problem. However, that isn't the case here. Going all-out by building classes for the trips, time strings would introduce more abstraction than what was required. This seemed like adding abstraction just for the sake of it, when the problem could be solved using existing objects and classes.
I used a simple approach instead, of using built-in objects. Python provides dictionaries and tuples objects. Dictionaries help store data in a key-value format, are mutable and provide quick reads (O(1)). I used tuples to store the trip data for each driver, as these are immutable, and can store data of different types. The structure only stores 3 values, so there is no issue in readability either. 

2. Reusability and Abstraction
While writing the code, I realized there is in fact some scope for reusability. It was possible to make some functions abstract and use them outside the scope of this problem. Thus, I created separate libraries of helper functions. These are some basic functions dealing with dictionaries, tuples and time strings, which can be used again if required. One would just need to import them to their code, as we do with libraries in Python.

3. Testing:
I created three classes for unit testing different sets of functions. The tests cover border cases and check how the functions operate for all the possible kinds of inputs. Some wrapper functions (that simply call other functions) are tested by performing integration tests on the code. For performing integration tests, I just provided different input files that cover some edge cases and some scenarios where the program could fail, and corrected my code accordingly.

