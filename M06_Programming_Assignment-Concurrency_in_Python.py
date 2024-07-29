#Carly Grubbs 7/28/2024
#M06 Programming Assignment -Concurrency in Python

#13.1
#Importing the needed libraries
from datetime import date, datetime
import multiprocessing
from time import sleep
import random

#Setting a variable to todays date
right_now = date.today()

#Setting up the string of the date
right_now_str = right_now.isoformat()

#Creating the txt file usint w for writing and t for text mode
with open ("C:\IvyTech\SDEV220\module6\currentdate.txt", "wt") as currentdate:
    currentdate.write(right_now_str)

#13.2
#Opening the currentdate.txt file and setting the information to currentdate_input
with open("C:\IvyTech\SDEV220\module6\currentdate.txt", "rt") as currentdate_input:
    currentdate_string = currentdate_input.read()

#Displaying the information from the file
print(currentdate_string)

#13.3
#Setting the current YMD from the txt file to a variable called date
date = datetime.strptime(currentdate_string, "%Y-%m-%d")

#Printing the date variable
print(date)

#15.1
#Setting up a module called current using # seconds to pause the program
def current(seconds):
    sleep(seconds)
    print("wait", seconds, "seconds, time is", datetime.utcnow())

#Displaying the current time after pausing the program for a random number of seconds
if __name__ == '__main__':
    for n in range(3):
        seconds = random.random()
        proc = multiprocessing.Process(target=current, args=(seconds,))
        proc.start()