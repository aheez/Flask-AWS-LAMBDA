from math import sqrt
import googlemaps, requests, json
from googlemaps import distance_matrix

DEBUG = True
# gmaps = googlemaps.Client(key=None)

class location():
    def __init__(self, longitude: float, latitude: float, priority, idx: int):
        self.longitude  = longitude
        self.latitude   = latitude
        self.priority = self.set_priority(priority)
        self.id = idx
        self.distance = 0
        self.cost = 0

    def set_priority(self, priority):
        if (priority == "H"):
            return 1
        elif (priority == "M"):
            return 2
        elif (priority == "L"):
            return 3
        else:
            return 3.5
    
    def set_distance(self, new_distance):
        self.distance = new_distance * 100
        self.set_cost(new_distance)

    def set_cost(self, weight:float):
        self.cost = weight * self.priority
    
    def get_coordinates(self):
        return (self.latitude, self.longitude)

def distance(start: location, end:location):
    return (sqrt((start.longitude - end.longitude) ** 2 + (start.latitude - end.latitude) ** 2))

# TODO: GOOGLE MAPS INTEGRATION FOR DISTANCE
def get_distance(start: location, end:list):
    if DEBUG:
        end_list = [x.get_coordinates for x in end]
        # response = distance_matrix(gmaps, start.get_coordinates(), end_list, mode="driving", units="metric")
        response= json.JSONDecoder('./RES_SAMPLE.json')
        distances = [response['rows'][0]['elements'][x]['distance']['value'] for x in range(len(response['rows'][0]['elements']))]
        
        if len(distances) != len(end):
            raise ValueError("API responce error")
        else:
            for i in range(len(end)):
                end[i].set_distance(distances[i])
    else:
        for location in end:
            location.set_distance(distance(start, location))

def gen_route(start:location, locations: list) -> list:
    sorted_list = update_cost(start, locations)
    route = []
    route.append(start)
    
    for i in range(len(sorted_list)):
        sorted_list = update_cost(route[i], sorted_list)
        route.append(sorted_list.pop())
    
    if len(route) != len(locations) + 1:
        print("Err")
    
    return route

def update_cost(start:location, end: list) -> list:
    # TODO: Fix this issue <list issue for updating the distance> 
    if DEBUG:
        map(lambda x: x.set_distance(get_distance(start, [x])), end)
    else:
        get_distance(start, end)
    return sorted(end, key=lambda x: x.cost)

def sort_locations(locations: list):
    return locations.sort(key=lambda x: x.weight)

def print_locations(locations: list):
    for i in range(len(locations)):
        print(locations[i].id, '\t', locations[i].longitude, '\t\t', locations[i].latitude, '\t\t', locations[i].distance)