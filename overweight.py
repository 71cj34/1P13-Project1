"""
Adam Woods. 400568048. Program contains overweight function.
"""

from TEAM_passenger_data import *
from TEAM_fleet_data import *
import _config

def overweight(passengerdata,fleetdata):
    """
    Converts txt file of fleet data into a formatted python list object

    :param path: Path of fleet txt file
    :return: List of formatted data of type matrix/nested list
    """
    count=0 # initiate count of overweight bags at 0
    count2 =0 # initiate second count of bags at 0
    s=0 #initiate index variable s at 0
    plane_list = []  # initiate list of planes as empty list
    for i in range(len(fleetdata)):
        # append an empty list to plane_list for every plane in fleet data
        plane_list.append([])

    for i in range (len(plane_list)):
        # variable x is set as the first entry in every list (plane name) in fleet data
        x = fleetdata[i][0]
        plane_list[i].append(x) # plane name appended to list in 2d list
        destination = fleetdata[i][5] # destination variable is set as destination for each plane
        for z in range (len(passengerdata)): # loop will check every passenger in passenger data 2D list
            if passengerdata[z][3] == destination: # checks if passenger destination matches plane destination
                if fleetdata[i][7] < passengerdata[z][6]: # checks if weight of passenger bags is over weight limit
                    count +=1 # if they are, one is added to both counts
                    count2 += 1
        plane_list[i].append(count) # count is added to the corresponding 2D list with its plane name
        count = 0 # first count is set to 0
        # note that count 2 continues accumulating and keeps track of total overweight bags
    passenger_list = [] # passenger data list is initiated as empty list
    for i in range(count2): # loop adds empty list to passenger list for every overweight bag
        passenger_list.append([])
    for i in range (len(passengerdata)):  #loop runs for each 2D list in passenger data
        destination2 = passengerdata[i][3] # destination2 variable is made equal to destination of passenger at index i in passenger data list
        for z in range (len(fleetdata)):# loop runs for every plane in fleet data
                if destination2 == fleetdata[z][5]: # checks if passenger is going to same destination as plane
                    if fleetdata[z][7] < passengerdata[i][6]:# checks if passenger's bag is over weight limitc
                        passenger_list[s].append(passengerdata[i][0]) # appends passenger's name
                        passenger_list[s].append(passengerdata[i][1]) # appends passenger last initial
                        passenger_list[s].append(passengerdata[i][2]) # appends passenger gate number
                        passenger_list[s].append(round(float(passengerdata[i][6]) - float(fleetdata[z][7]),1)) # appends amount that the passenger's bag is overweight
                        s+=1 #one is added to s so that info is appended to next empty list in 2D list for following iteration of loop
    return plane_list, passenger_list # returns both plane and passenger lists
fleetdata = fleet_data(_config.fleet_data_path)
passengerdata = passenger_data(_config.passenger_data_path)

if __name__ == "__main__":
    for i in range(2):
        print(overweight(passengerdata,fleetdata)[i])

