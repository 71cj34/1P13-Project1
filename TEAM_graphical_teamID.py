"""
Uses turtle to print out a summary of all the other airplane functions

Thurs44, DS Project 1 ♡
"""

import _config
from daily_data import *
from oversold import *
from overweight import *
from layover import *
from TEAM_passenger_data import *
from TEAM_fleet_data import *
from time_delay import *
import turtle as t

t.setup(1500, 500)
screen = t.Screen()
screen.title("graphical_44")

t = t.Turtle()
t.hideturtle()
t.speed(0)

# format for input lists
# time_delay: [[model, # of lates], ...]
# layover: [[model, # of layover], ...] [0] only
# overweight: [[model, # of overweight], ...] [0] only
# oversold: [[model, # of oversold], ...] [0 and 1]

def graphical_44(time_delay, layover, overweight, b_oversold, e_oversold):
    """
    Prints out a graphical representation of the airplane functions

    :param time_delay: 2D List of models, number of delayed passengers
    :param layover: 2D List of models, number of layovers
    :param overweight: 2D List of models, overweight passengers
    :param b_oversold: 2D List of models, business class oversold seats
    :param e_oversold: 2D List of models, economy class oversold seats
    :return: None
    """
    concat_inputs = [time_delay, layover, overweight, b_oversold, e_oversold] # semi-elegant solution for list iteration
    concat_inputs_names = ["Late & Layovers", "Layovers", "Overweight", "Business Oversold", "Economy Oversold"]
    if len(time_delay) == len(layover) == len(overweight) == len(b_oversold) == len(e_oversold):
        for i in range(len(time_delay)): # for every plane model
            current_model = time_delay[i][0].strip()
            coordinates = [-750 + 150*(i+1), 150] #x: 125 blocks 25 padding, y: 30 rect, 10 padding, 52 each x 5
            # Turtle writing script
            t.up()
            t.goto(coordinates[0], coordinates[1])
            t.color("chartreuse") # a whimsical color
            t.down()
            t.begin_fill()
            t.setheading(270)
            t.forward(30)
            t.setheading(0)
            t.forward(125)
            t.setheading(90)
            t.forward(30)
            t.setheading(180)
            t.forward(125)
            t.end_fill()
            t.color("black")
            t.up()
            t.setheading(270)
            t.forward(20)
            t.down()
            t.write(current_model)
            t.up()
            t.goto(coordinates[0], t.pos()[1] - 40)
            t.down()
            for j in range(0, len(concat_inputs)): # for every single input list
                # plane_index = concat_inputs[j].index(current_model)
                plane_index = None
                for k in range(len(concat_inputs[j])): # trawl through every sublist in every list to find the plane model
                    if concat_inputs[j][k][0] == current_model:
                        plane_index = k
                if plane_index == None: # just in case the model is not found
                    raise ValueError(f"Model {current_model} could not be found in one or more input lists!")
                # get value + its name
                current_value = concat_inputs[j][plane_index][1]
                current_value_name = concat_inputs_names[j]
                t.write(arg=(str(current_value_name + ": " + str(current_value)))) # Write one element including title
                t.up()
                t.goto(coordinates[0], t.pos()[1] - 22)
    else:
        raise ValueError("Length mismatch in input lists")

    screen.exitonclick()
    t.done()

if __name__ == "__main__":
    fleet_info = fleet_data(_config.fleet_data_path)
    passenger_info = passenger_data(_config.passenger_data_path)
    graphical_44(
                 time_delay(fleet_info, passenger_info),
                 layover(passenger_info, fleet_info)[0],
                 overweight(passenger_info, fleet_info)[0],
                 oversold(passenger_info, fleet_info, daily_data(passenger_info))[0],
                 oversold(passenger_info, fleet_info, daily_data(passenger_info))[1]
                 )
