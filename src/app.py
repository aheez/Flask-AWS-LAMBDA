import random
from classes import *

priority_list = ["H", "M", "L"]
NO_LOCATIONS = 10

mainWH = location(longitude=26.305201, latitude=50.149044, priority="L", idx=0)
# mainWH (26.305201, 50.149044)
# mainWH_gmaps = gmaps.geocode(mainWH.longitude, mainWH.latitude)

MAX = (26.463428, 50.184721)
MIN = (26.273890, 50.025944)

maximum = (1e4 * (MAX[0] - MIN[0]))
minimum = (1e4 * (MAX[1] - MIN[1]))

temp_long = [random.randint(10, int(maximum)) / 1e4 + MIN[0] for x in range(NO_LOCATIONS)]
temp_lati = [random.randint(10, int(minimum)) / 1e4 + MIN[1] for x in range(NO_LOCATIONS)]

# test_locations = [location(longitude=temp_long[i], latitude=temp_lati[i], priority=priority_list[random.randint(0, 2)], idx= i + 1) for i in range(NO_LOCATIONS)]
test_locations = [
	(26.323264, 50.161992, 'L', 100),			# Test location 1 (Rayeg)
	(26.334951, 50.191867, 'H', 200),
	(26.373389, 50.236519, 'M', 300)			# 5751 نفيس بن هلال،, الصدفة، 8750, الخبر 34215
]

test_locations = [location(x[0], x[1], x[2], x[3]) for x in test_locations]

# for i in range(len(test_locations)):
# 	test_locations[i].set_distance(distance(mainWH, test_locations[i]))
# 	print(test_locations[i].weight)

# map(lambda x: x.set_distance(distance(mainWH, x)), test_locations)
# print_locations(test_locations)

# TODO: Sort them
# sorted_set = sort_locations(test_locations)
# sorted_set = sorted(test_locations, key=lambda x: x.cost)
# temp = [x.weight for x in test_locations]
# temp = temp.sort()
# for i in range(len(temp)):
# 	for j in range(len(test_locations)):
# 		if (test_locations[j].weight == temp[i]):
# 			sorted_set.append(test_locations[j])
# 			break

# new_order = [] 
# for i in range(len(test_locations)):
# 	new_order.append(sorted_set.pop())
# 	map(lambda x: x.set_distance(distance(new_order[i],x)), sorted_set)
# 	sorted_set = sorted(sorted_set, key=lambda x: x.cost)
# 	print("\n", i, "Pass:")
# 	print_locations(sorted_set)

route = gen_route(mainWH, test_locations)
print('\n\nSorted:')
# print_locations(sorted_set)
print_locations(route)

# TODO: GOOGLE MAPS INTEGRATION