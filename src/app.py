import random
from classes import *

priority_list = ["H", "M", "L"]
NO_LOCATIONS = 10

mainWH = location(longitude=26.305201, latitude=50.149044, priority="L", idx=0)

MAX = (26.463428, 50.184721)
MIN = (26.273890, 50.025944)

maximum = (1e4 * (MAX[0] - MIN[0]))
minimum = (1e4 * (MAX[1] - MIN[1]))

temp_long = [random.randint(10, int(maximum)) / 1e4 for x in range(NO_LOCATIONS)]
temp_lati = [random.randint(10, int(minimum)) / 1e4 for x in range(NO_LOCATIONS)]

test_locations = [location(longitude=temp_long[i], latitude=temp_lati[i], priority=priority_list[random.randint(0, 2)], idx= i + 1) for i in range(NO_LOCATIONS)]

for i in range(len(test_locations)):
	test_locations[i].set_weight(distance(mainWH, test_locations[i]))

for i in range(len(test_locations)):
	print(test_locations[i].weight)