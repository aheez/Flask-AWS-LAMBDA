from math import sqrt
import googlemaps, requests, json
from googlemaps import distance_matrix

gmaps = googlemaps.Client(key=None)

class location():
    def __init__(self, longitude: float, latitude: float, priority, idx: int):
        self.longitude  = longitude
        self.latitude   = latitude
        self.priority = self.set_priority(priority)
        self.id = idx
        self.distance = 0xFFFF
        self.weight = 0xFFFFFFFF

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
        self.distance = new_distance
        self.set_weight(new_distance)

    def set_weight(self, unscaled:float):
        self.weight = unscaled * self.priority
    
    def get_coordinates(self):
        return (self.latitude, self.longitude)

def distance(start: location, end:location):
    return (sqrt((start.longitude - end.longitude) ** 2 + (start.latitude - end.latitude) ** 2))

# TODO: GOOGLE MAPS INTEGRATION FOR DISTANCE
def get_distance(start: location, end:list):
    end_list = [x.get_coordinates for x in end]
    response = distance_matrix(gmaps, start.get_coordinates(), end_list, mode="driving", units="metric")
    distances = [response['rows'][0]['elements'][x]['distance']['value'] for x in range(len(response['rows'][0]['elements']))]
    
    if len(distances) != len(end):
        raise ValueError("API responce error")
    else:
        for i in range(len(end)):
            end[i].set_distance = distances[i]

def sort_locations(locations: list):
    return locations.sort(key=lambda x: x.weight)

def print_locations(locations: list):
    for i in range(len(locations)):
        print(locations[i].id, '\t', locations[i].longitude, '\t\t', locations[i].latitude, '\t\t', locations[i].weight)