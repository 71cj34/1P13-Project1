from TEAM_passenger_data import *
from TEAM_fleet_data import *
from daily_data import *
import _config

"""
Finds how many passengers are late and sorts by flight

chenj692, 2024, 400565775
"""
def time_delay(fleet, passengers):
    """
    Reads if a flight is delayed, and finds how many passengers are on that flight.

    :param fleet: Nested list object of fleet data
    :param passengers: Nested list object of passenger data
    :return: Nested list object of pairwise flight/passenger number data
    """
    final_output = []
    for plane in fleet:
        late_count = 0
        gate_destination = [plane[4], plane[5]]
        is_late = True if plane[6] == "Late" else False
        plane_model = plane[0]
        for passenger in passengers:
            # This file includes support for all three format types.
            if len(passenger[3]) == 1:  # eliminate possibility of v1 via checking if class is at index 3
                format_locations = [passenger[2], passenger[4]]
            elif "-" not in passenger[3]:  # eliminate possibility of v2 by checking if dest. is at index 3
                format_locations = [passenger[2], passenger[3]]
            else:  # must be v3
                format_locations = [passenger[3], passenger[5]]
            if format_locations == gate_destination:
                if is_late and passenger[7] != "":
                    late_count += 1
        final_output.append([plane_model, late_count])

    return final_output
    # cursed codegolf version
    # return [[i[0], sum([i[6] == "Late" and [j[2], j[4]] == [i[4], i[5]] for j in passengers])] for i in fleet]

if __name__ == "__main__":
    # print("Raw fleet data: ", fleet_data(_config.fleet_data_path))
    # print("Raw passenger data (v1): ", passenger_data("passenger_data_v1.txt"))
    # print("Time delay count (should be the same for all three!)", time_delay(fleet_data(_config.fleet_data_path), passenger_data("passenger_data_v1.txt")))

    # print("Raw fleet data: ", fleet_data(_config.fleet_data_path))
    # print("Raw passenger data (v2): ", passenger_data("passenger_data_v2.txt"))
    print(time_delay(fleet_data(_config.fleet_data_path), passenger_data("passenger_data_v2.txt")))


    # print("Raw fleet data: ", fleet_data(_config.fleet_data_path))
    # print("Raw passenger data (v3): ", passenger_data("passenger_data_v3.txt"))
    # print("Time delay count (should be the same for all three!)", time_delay(fleet_data(_config.fleet_data_path), passenger_data("passenger_data_v3.txt")))
