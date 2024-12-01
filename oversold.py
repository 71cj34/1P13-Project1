# -*- coding: utf-8 -*-
"""
Madelaine Templeman
400575355

This program accpets lists from functions passenger data, fleet data, and daily data to
calculate the number of tickets in buisness and economy class that have been oversold.
Two lists are returned with the plane and gates and oversold seats.
"""

from TEAM_passenger_data import *
from TEAM_fleet_data import *
from daily_data import *
import _config


def oversold(passenger_list, fleet_list, daily_list):
    """
    Calculates how many oversold passengers are on each flight
    """
    oversold_business_seats = []
    oversold_economy_seats = []

    for sub_list in fleet_list:  # go through each list to find flight information required
        plane_model = sub_list[0]
        plane_gate = sub_list[4]
        business_seats = int(sub_list[1])#convert to integer values so math can be done with them
        economy_seats = int(sub_list[2])

        business_oversold = 0
        economy_oversold = 0

        for sub_list_b in daily_list:  # filter through the lists within daily_data

            if sub_list_b[0] == plane_gate:  # find the right plane by finding list with corresponding gate number
                """need to convert my numbers to integers before math can be done.
                everything being taken out of a list starts as a string"""
                business_oversold = business_seats - int(
                    sub_list_b[1])  # differance between seats available and seats sold
                if business_oversold < 0:  # if the number of seats sold is greater than available seats
                    business_oversold = abs(business_oversold)
                else:
                    business_oversold = 0

                economy_oversold = economy_seats - int(sub_list_b[2])
                if economy_oversold < 0:
                    economy_oversold = abs(economy_oversold)
                else:
                    economy_oversold = 0
                break  # Once the correct gate is found, no need to check further

        business_list = [plane_model, business_oversold]
        economy_list = [plane_model, economy_oversold]
        oversold_business_seats.append(business_list)
        oversold_economy_seats.append(economy_list)

    return oversold_business_seats, oversold_economy_seats # Return both lists


if __name__ == "__main__":
    # Assuming passenger_data and fleet_data functions are defined elsewhere
    # and daily_data is a function that processes passenger_data to generate daily_list
    passenger_data_raw = passenger_data(_config.passenger_data_path)
    fleet_data_raw = fleet_data(_config.fleet_data_path)
    for i in range(2):
        print(oversold(passenger_data_raw, fleet_data_raw, daily_data(passenger_data_raw))[i])
