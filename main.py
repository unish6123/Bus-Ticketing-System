from passengerinfo import*
from showTicket import*

global ch # Declared a global variable

print("------------------------------------------")
print("------------Welcome to NJ Transit---------")
print("------------------------------------------")
print()

def start():
    print('Press "1" if you want to book your ticket.')
    print('Press "2" if you want to view your ticket.')
    ch = input("Choose one option: ")
    try: 
        ch = int(ch)
    except:
        ch = ch
    if ch == 1:
        pd_obj = PassengerDataCsv()
        pd_obj.passengerInfo()
        pd_obj.saveInfo()
    elif ch == 2:
        obj = TicketShow()
        obj.showTicket()
    else:
        print("Enter a valid option: ")
        start()
start()

