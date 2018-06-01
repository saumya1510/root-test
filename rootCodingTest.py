import sys
from timestringFunctions import findTimeDifference
from objectHelperFunctions import addValuesFromTuples, sortDictionaryByValues

"""
Reads an input file provided as a command line argument, containing details of drivers and their trips. 
Writes to another file called "output" the average speed and distance travelled by each driver.
"""

def updateDriversMap(driversMap, key, value):
	"""
	Updates the dictionary by adding a new driver, or updating the distance and time values.
	Args:
		driversMap: Dictionary object
		Key, Value: Key => Driver name, Value => (distance, time), (0,0) if new driver.
	Returns:
		driversMap if updated successfully, else None.
	"""
	if key not in driversMap:
		if value != (0, 0):
			print("Driver not registered. Moving on.")
			return None
		else:
			driversMap[key] = value
			return driversMap
	else:
		curValue = driversMap[key]
		driversMap[key] = addValuesFromTuples(curValue, value)
	return driversMap

def checkTripSpeed(distance, time, lowerLimit = 5, upperLimit = 100):
	"""
	Given the distance and time, the function returns True if the speed is within the limits provided.
	Args:
		Distance, Time, Lower Limit, Upper Limit.
	Returns:
		Boolean: True if the speed is within the limits, else False.
	"""
	if not time:
		print("Time is 0!")
		return False
	if distance/time < lowerLimit or distance/time > upperLimit:
		return False
	return True

def getTimeAndDistance(parameters):
	"""
	Wrapper function to parse the parameters from the dictionary and get the time taken and distance travelled.
	Args:
		Parameters: List of values for the trip: Distance, start time, end time.
	Returns:
		(Distance, Time Taken): Tuple containing the distance travelled and time taken
	"""
	timeTaken = findTimeDifference(parameters[0], parameters[1])
	if checkTripSpeed(float(parameters[2]), timeTaken, 5, 100):
		return (float(parameters[2]), timeTaken)
	return None

def readFile(fileName):
	"""
	Reads the input file and parses it into a Python Dictionary. 
	Arg:
		fileName: name of the input file which would be read by the function.
	Returns:
		driversMap: Dictionary object of the form  {key: value} where:
						key = name of the driver, 
						values = (total distance, total time)
	"""
	driversMap = {}
	try:
		with open(fileName, 'r') as f:
			for line in f:
				line = line.strip("\n")
				command = line.split(" ")[0]
				parameters = line.split(" ")[1:]
				if command == "Driver":
					value = (0, 0)
				else:
					value = getTimeAndDistance(parameters[1:])		
					if not value:
						continue			
				updateDriversMap(driversMap, parameters[0], value)
	except EnvironmentError as e:
		print("Unable to open file. Error: " + str(e))
	return driversMap


def writeToFile(driversMap):
	"""
	Writes the content of the list of tuples to a file in the required format.
	Args:
		reportList: List of tuples containing name of the driver, distance travelled and average speed.
	Returns:
		Boolean: True if successfully written, else False.
	"""
	try:
		with open('output', 'w') as outFile:
			for key in sortDictionaryByValues(driversMap, 1, True):
				values = driversMap[key]
				if values[1]:
					avgSpeed = round(values[0]/values[1])
				else:
					avgSpeed = 0
				outFile.write("{0}: {1} miles @ {2} mph\n".format(key, round(values[0]), avgSpeed))
		return True
	except IndexError:
		print("Not a valid list of tuples.")
		return False


def main():
	"""
	Driver function for the program. Reads a system argument (input file), and 
	writes the output to a file called "output".
	"""
	try:
		fileName = sys.argv[1]
	except IndexError:
		print("Filename not provided. Terminating.")
		return
	print("Reading file...")
	driversMap = readFile(fileName)
	print(driversMap)
	if len(driversMap):
		writeToFile(driversMap)

if __name__ == '__main__':
	main()