from objects import *
from objects_2 import *
from graphic import show_city, show_towers_and_signal, i_wanted_path

# Enter the size of your desired city here
city_size = (15, 15)

# Set this variable to the desired percentage of cells blocked for towers
percentage_of_occurrence_of_blocked_blocks = 30

# Assign a value to the towers' range of action or fill in the list of specific values
tower_operating_radius = 2
tower_operating_radius_list = [2, 3]

# Uncomment this function if you want to see all the beauty of the created city
# WARNING!!! Your GPU may be enjoying this function too much.

# show_city(city_size[0],
#           city_size[1],
#           percentage_of_occurrence_of_blocked_blocks,
#           tower_operating_radius)

# Uncomment this function to see the towers, the signal they give out and blocked blocks

# show_towers_and_signal(city_size[0],
#                        city_size[1],
#                        percentage_of_occurrence_of_blocked_blocks,
#                        tower_operating_radius)

# To get a path from one tower to another, enter the tower numbers and uncomment this function
# The result will be output to the console

# P.S. Despite the fact that the algorithm filled the city with towers so that at each point
# there is access to at least 3 towers, it is often impossible to create a path since the
# towers are combined into groups within which the signal cannot leave, so be patient and
# try several times to see the result

path = (1, 12)

i_wanted_path(city_size[0],
              city_size[1],
              path,
              percentage_of_occurrence_of_blocked_blocks,
              tower_operating_radius)
