"""
Laa1

daily_data() function

"""

from TEAM_passenger_data import *
import _config

#A Function to read and process passenger data from a file
# def read_passenger_data():
#     """
#     Reads passenger data from a text file and returns it as a list of lists.
#     Each line in the file is split by commas and stored as a list entry.
#
#     """
#     file = open("passenger_data_v2.txt", "r")
#
#     passenger_list = [] #An empty list to store passenger data
#
#     for line in file: #Read lines from the file, processing each of the lines, and adding to the list
#
#         passenger_list.append(line.strip().split(","))
#
#     file.close()
#
#     return passenger_list #Return the processed list of passenger data


#A Function to process daily boarding data
def daily_data(passengers):
    """
    Calculates the number of passengers boarding in Business (B) and Economy (E) classes for each day.

    """
    daily_summary = [] #Initialize a list to hold daily data

    #Go through each passenger's data starting from the second row
    
    for passenger in passengers[1:]: #Skip the header row since (passengers[0])
        date = passenger[2] #Take the date
        class_type = passenger[4] #Take the class type (B or E)

        #Find an entry for the current date in the daily_summary list
        for record in daily_summary:
            if record[0] == date: 
                #Update counts based on the passenger's class type
                if class_type == "B":
                    record[1] += 1 #Business counter
                elif class_type == "E":
                    record[2] += 1 #Economy counter 
                else:
                    print("Sorry, invalid class type", class_type)
                break #Exit loop when the date gets found
        else:
            #If the date is not found then make create a new entry for this date
            if class_type == "B":
                daily_summary.append([date, 1, 0]) #Start with 1 business passenger
            elif class_type == "E":
                daily_summary.append([date, 0, 1]) #Start with 1 economy passenger
            else:
                print("Sorry, invalid class type", class_type)

    return daily_summary


# Main section  that can be used for testing
if __name__ == "__main__":
    passengers = passenger_data(_config.passenger_data_path) #read the passanger data from the file
    daily_summary = daily_data(passengers) #Process the daily data summary

    # print("Daily Boarding Summary:") #results to user
    # for record in daily_summary:
        # print(f"Date: {record[0]}, Business: {record[1]}, Economy: {record[2]}")
    print(daily_summary)
