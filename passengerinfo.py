import csv

class Registration:
    def __init__(self):
        self.passengerName = None
        self.passengerNum = None
        self.departure = None
        self.destination = None
        self.ddmmyyyy = None
        self.seatNo = None
        self.busType = None
        self.fare = None
        self.autoInc = 1
        self.countCol = 0

    def passengerInfo(self):
        self.passengerName = input('Enter traveller name: ')
        self.passengerNum = input('Enter the number of traveller: ')
        print("Enter the following number of corresponding location")
        print("1 for Newyork")
        print("2  for Caldwell")
        print("3: for Bloomfield.")

        loc = int(input("enter a destionation number: "))
        if loc == 1:
            self.destination = "Newyork"
        elif loc == 2:
            self.destination = "Caldwell"
        elif loc == 3:
            self.destination = "Bloomfield"
        
        self.ddmmyyyy = input("Enter the travelling date in 'dd/mm/yyyy' formate: ")

        # Bus seats
        print("1---2---3---4---5---6---7---8---9---10")
        print("11---12---13---14---15---16---17---18---19---20")

        seatNoList = [i for i in range(1,21)]
        self.bookingList = []
        def bookSeat():
            while True:
                self.seatNo = int(input("Choose a seat number:"))
                if self.seatNo <= 20:
                    if self.seatNo in seatNoList:
                        self.bookingList.append(self.seatNo)
                        del seatNoList[self.seatNo-1] 
                        count = len(seatNoList)
                    else:
                        print("Ticket is already booked")
                    print("Do you want to book more seats Enter (Yes/No")
                    y = input(" Enter ")
                    if y.lower() == 'yes':
                        bookSeat()

                        
                    else:
                        break
                else:
                    print("Choose a valid seat Number.")
                    bookSeat()
# SELECTING BUSTYPE AND CALCULATING FARE
        
        print("1. AC BUS = $2")
        print("2. For Non- AC bus = $3")

        self.bus = int(input("Enter your desired bus Type: "))

        if self.bus == 1:
            self.bustType = "AC Bus"
            self.fare = self.passengerNum * 2

        elif self.bus == 2:
            self.busType = "Non AC Bus"
            self.fare = self.passengerNum * 3


# Storing Passenger Info as well as Tickets in CSV.\
class PassengerDataCsv(Registration):
    def saveInfo(self):
        try:
            with open("passengerData.csv", 'r+', newline = "") as f:
                r = csv.reader(f)
                data = list(r)
                # print(self.data)
                for i in data:
                    self.autoInc += 1
                    for j in i:
                        self.countCol += 1
                    print()
                print("Number of Records are found in Database:", self.autoInc)
        except:
            print("File is not available")
        finally:
            with open("passengerData.csv", 'a+', newline = "") as f:
                w = csv.writer(f)
                
                w.writerow([self.autoInc, "Atlantic City", self.passengerName, self.passengerNum, self.destination, self.ddmmyyyy,self.busType,self.fare, self.seatNo])
                print("Data saved Successfully")







