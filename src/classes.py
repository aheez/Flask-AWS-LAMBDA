from math import sqrt
import googlemaps, requests, json

gmaps = googlemaps.Client(key=None)

class location():
    def __init__(self, longitude: float, latitude: float, priority, idx: int):
        self.longitude  = longitude
        self.latitude   = latitude
        self.priority = self.set_priority(priority)
        self.id = idx
        self.distance = 0xFF
        self.weight = 0xFFFFFFFF

    def set_priority(self, priority):
        if (priority == "H"):
            return 10
        elif (priority == "M"):
            return 20
        elif (priority == "L"):
            return 30
        else:
            return 35
    
    def set_weight(self, unscaled:float):
        self.weight = unscaled * self.priority

def distance(start: location, end:location):
    return (sqrt((start.longitude - end.longitude) ** 2 + (start.latitude - end.latitude) ** 2))

# TODO: GOOGLE MAPS INTEGRATION FOR DISTANCE
# def get_distance(start: location, end:location):


def sort_locations(locations: list):
    return locations.sort(key=lambda x: x.weight)

def print_locations(locations: list):
    for i in range(len(locations)):
        print(locations[i].id, '\t', locations[i].longitude, '\t\t', locations[i].latitude, '\t\t', locations[i].weight)