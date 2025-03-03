# list important dates and how many days until they arrive. 

import datetime
from datetime import date
events =[]

class Event: 
    def __init__(self, name, day, month , year =2025):
        self.name = name 
        self.date = datetime.date(year, month, day) 
        events.append(self) 
    def __str__(self):
        return self.name +": " +str( self.date)+": " +str(self.daysOut())+" days away\n"   
    def daysOut(self):
        return (self.date - date.today())

dataMeeting = Event("Data meeting" , 6, 3)
lastDay = Event("Last day of school" , 24, 6) 
fiveWkEnd = Event("5 week end" , 14, 3)
taxDay = Event("Tax day" , 15, 4) 
print("Important upcoming events:")
for event in events: 
    print(event) 
