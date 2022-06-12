from math import sqrt

class location():
    def __init__(self, longitude: float, latitude: float, priority, idx: int):
        self.longitude  = longitude
        self.latitude   = latitude
        self.priority = self.set_priority(priority)
        self.id = idx
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
    
    def set_weight(self, unscaled:float):
        self.weight = unscaled * self.priority

def distance(start: location, end:location):
    return (sqrt((start.longitude - end.longitude) ** 2 + (start.latitude - end.latitude) ** 2))