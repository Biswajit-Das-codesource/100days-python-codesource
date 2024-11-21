'''
How to show current time using python 

    1.download datetime( pip install datetime)
    2.now we use the date time method on our program  
    
'''
import datetime #import the datetime 

nowdate=datetime.datetime.now() #now is used for the give the current date time 

currentTime = nowdate.strftime("%H:%M:%S")

'''strftime is used for give the string value of the time  
H is stands for the hour 
M is stands for the minute
S is stands for the second'''

print("Current Time =", currentTime)



