"""
Adam Woods, woodsa18

Code to see how many people are overweight, DS1
"""

from TEAM_passenger_data import *
from TEAM_fleet_data import *
import _config

def overweight(passengerdata,fleetdata):
    """
    Checks how many passengers are over weight on all flights
    """
    count=0
    count2 =0
    s=0
    plane_list = []
    for i in range(len(fleetdata)):
        plane_list.append([])

    for i in range (len(plane_list)):
        x = fleetdata[i][0]
        plane_list[i].append(x)
        destination = fleetdata[i][5]
        for z in range (len(passengerdata)):
            if passengerdata[z][3] == destination:
                if fleetdata[i][7] < passengerdata[z][6]:
                    count +=1
                    count2 += 1
        plane_list[i].append(count)
        count = 0
    passenger_list = []
    for i in range(count2):
        passenger_list.append([])
    for i in range (len(passengerdata)):
        destination2 = passengerdata[i][3]
        for z in range (len(fleetdata)):
                if destination2 == fleetdata[z][5]:
                    if fleetdata[z][7] < passengerdata[i][6]:
                        passenger_list[s].append(passengerdata[i][0])
                        passenger_list[s].append(passengerdata[i][1])
                        passenger_list[s].append(passengerdata[i][2])
                        passenger_list[s].append(round(float(passengerdata[i][6]) - float(fleetdata[z][7]),1))
                        s+=1
    return plane_list, passenger_list

fleetdata = fleet_data(_config.fleet_data_path)
passengerdata = passenger_data(_config.passenger_data_path)

if __name__ == "__main__":
    for i in range(2):
        print(overweight(passengerdata,fleetdata)[i])
