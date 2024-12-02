"""
naserf1 400576574

Layover function for DS1. Sorts by flight, and outputs how many people are on layovers.
"""

from TEAM_passenger_data import *
from TEAM_fleet_data import *
import _config

def layover(passenger_data, fleet_data):
    """
    Finds now many people are affected by layovers by flight

    """
    # initialize the lists
    layover_counts = []
    layover_passengers = []

    # go through each plane in fleet_data
    for plane in fleet_data:
        model = plane[0]
        gate = plane[4]
        count = 0

        # check passengers for this plane's gate
        for passenger in passenger_data:
            if passenger[2] == gate:  # does the passenger's gate match this plane's gate?
                if passenger[7] == "Layover":  # does the passenger have layover?
                    count += 1
                    # save passenger's name, first letter of last name and gate
                    layover_passengers.append([passenger[0], passenger[1][0], passenger[2]])

        # add plane model and its layover count to the result list
        layover_counts.append([model, count])

    return layover_counts, layover_passengers

if __name__ == "__main__":
    # print(passenger_data(_config.passenger_data_path))
    # print(fleet_data(_config.fleet_data_path))
    for i in range(2):
        print(layover(passenger_data(_config.passenger_data_path), fleet_data(_config.fleet_data_path))[i])
