from passengerinfo import Registration, PassengerDataCsv
import csv
class TicketShow:
    def showTicket(self):
        dataStore = []
        with open("passengerData.csv", 'r+', newline = "") as f:
            r = csv.reader(f)
            # data = list(r)
            id = int((input("Enter your booking Id: ")))
            for eachline in r: #data lekhya they paila
                if id == int(eachline[0]):
                    for  lineElements in eachline:
                        dataStore.append(lineElements)
                    break

        print("------------------------------------------------------------------")
        print("                     NJ TRANSIT                      ")
        print("----------------------------------------------------------")
        print()
        print("", dataStore[1],"---------->", dataStore[4],"        ","   Passenger ID: ",dataStore[0])
        print()
        print("Passenger Name: ", dataStore[2], "            ","     Number of Passengers: ", dataStore[3])
        print("-------------------------------------------------------")

        print()
        print("Booking Date: ", dataStore[5], "                ","    Seat No: ", dataStore[8],"          ")
        print()
        print("Bus Type:       ", dataStore[6])
        print("Bus Fare:       ", dataStore[7])
        print()
        print("-------------------------------------------------------------")
