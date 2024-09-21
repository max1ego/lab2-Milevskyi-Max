import sys

fullnum = int(input("4-digit number:"))
floatnum = fullnum / 100
firsthalf = int(floatnum)
secondhalf = int(round(floatnum - firsthalf, 2) * 100)
print(firsthalf)
print(secondhalf)
