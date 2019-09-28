import os
from colorama import Fore, Back, Style
from datetime import timedelta, datetime


# global values
event_list = []
class Event:
    def __init__(self, id, name, date, place):
        self.id = id,
        self.name = name,
        self.date = date,
        self.place = place
    
def registration():    
        id = int(input("Enter event ID:"))
        name = input("Enter event Name:")
        date = datetime.strptime(input("Enter event Date:"),"%d/%m/%Y")
        place = input("Enter event Place:")
        event = Event(id, name, date, place)
        return event

def list_events():
    print("Event list")
    for item in event_list:
        print("Event ID:", item.id)
        print("Event Name:", item.name)
        print("Event Date:", item.date)
        print("Event Place:", item.place)
        print("------------")
        print()

def menu():
    option = None   

    while option != 0:     
        # os.system("cls")
        print()
        print(Fore.WHITE, Back.RED +"-------------Welcome to Event Registration------------------")
        print(Style.RESET_ALL)

        print("-------Menu-------")
        print()
        print("1. Register")
        print()
        print("2. Show Registration")
        print()
        print("0. Exit")
        print()    
        option = int(input("Choose option:"))        

        if(option == 1):
            print("Registration")
            event = registration()                                   
            event_list.append(event)
        
        if(option == 2):
            list_events()
            hold = input("press any key..")

menu()

