"""
Functions for manipulating, and operating on time strings (hh:mm, 24 hour format).
"""
def splitTimeString(time):
	"""
	Takes a 24-hour time string of the form hh:mm and splits them into hours and mins. 
	Args:
		time: String of the format hh:mm, 24 hours.
	Returns:
		hour, mins: integers representing hours (24-hour format) and minutes. 
	"""
	try:
		hour, mins = map(int, time.split(':'))
		return hour, mins
	except Exception as e:
		print(e)
		return None

def findTimeDifference(start, end):
	"""
	Finds difference between any two time-strings of the format hh:mm (24-hour).
	Args:
		start, end: Strings of format hh:mm, where start <= end
	Returns:
		timeTaken: Float value of the time passed in hours. 
					Eg. 10.5: 10 hours and 30 minutes. 
						0.5: 30 minutes.
	"""
	startHour, startMins = splitTimeString(start)
	endHour, endMins = splitTimeString(end)
	if endHour < startHour:
		print("Start time should be before the end time.")
		return
	timeTaken = (endHour + endMins/60) - (startHour + startMins/60) 
	return timeTaken