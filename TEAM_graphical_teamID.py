from daily_data import *
from oversold import *
from overweight import *
from TEAM_passenger_data import *
from TEAM_fleet_data import *
from time_delay import *

import turtle as t
t.setup(1500, 500)
screen = t.Screen()
screen.title("graphical_44")

t = t.Turtle()

# time_delay: [[model, # of lates], ...]
# layover: [[model, # of layover], ...]
# overweight: [[model, # of overweight], ...]
# oversold: [[model, # of oversold (business)], ...]

def graphical_44(time_delay, layover, overweight, b_oversold, e_oversold):
    concat_inputs = [time_delay, layover, overweight, b_oversold, e_oversold]
    concat_inputs_names = ["Time Delay", "Layover", "Overweight", "Business Oversold", "Economy Oversold"]
    if len(time_delay) == len(layover) == len(overweight) == len(b_oversold) == len(e_oversold):
        for i in range(len(time_delay)): # for every plane model
            current_model = time_delay[i][0]
            coordinates = [-750 + 150*(i+1), 150] #x: 125 blocks 25 padding, y: 30 rect, 10 padding, 52 each x 5
            t.teleport(coordinates[0], coordinates[1])
            t.color("chartreuse")
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
            t.write(current_model)
            t.teleport(y=t.pos()[1] - 40)
            for j in range(0, len(concat_inputs)): # for every single input list
                plane_index = concat_inputs[j].index(current_model)
                current_value = concat_inputs[j][plane_index][1]
                current_value_name = concat_inputs_names[j]
                t.write(arg=(current_value_name, ": ", current_value))
                t.teleport(y=t.pos()[1] - 52)
    else:
        raise ValueError("Length mismatch in input lists")

    screen.exitonclick()
    t.done()

if __name__ == "__main__":
    graphical_44()
