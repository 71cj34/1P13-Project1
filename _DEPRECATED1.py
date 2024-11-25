# [[name, initial, flight num, dest, seat class, status, baggage weight, arrival status], ...]
# [[gate [2], # business [4], # econ], ...]

def daily_data(passenger_data):
    final_output = []
    for i in range(len(passenger_data)):
        current_gate = passenger_data[i][2]
