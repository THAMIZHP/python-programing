'''
3. Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
'''
#solution
import datetime
time=datetime.datetime.now()
print("DATE",time.strftime("%Y-%m-%d"),sep=":",)
print("TIME",time.strftime("%H:%M:%S"),sep=":")
