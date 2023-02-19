from typing import Tuple
import numpy as np
import datetime
import urllib.request
import json
from geopy.geocoders import Nominatim
import random

"""
USAGE
On startup, instantiate a single Analysis object
On checking pings, call Analysis.update()
On user ratings, call Analysis.rate_location()

Site should periodically refresh to see if the scores have changed:
1. check Analysis.tick to see if it has increased since last score
2. check Analysis.state for STATE_NORMAL -- optionally, handle/display error (should ignore for hackathong)
3. check Analysis.processed for True     -- if False, keep waiting and maintaing previous tick
4. call Analysis.get_location_scores()
"""

API_KEY = "f829251927f392ec48f72dc2c8098c6a"
MODE    = 0
LOCATIONS = [
    "UgLi",
    "Hatcher",
    "Union",
    "LSA",
    "League",
    "Fishbowl",
    "Ross",
    "IM"
]

def get_device_latlong(ping) -> Tuple[int, int]:
    route      = urllib.request.urlopen(f"http://api.ipapi.com/api/{ping}?access_key={API_KEY}").read().decode("utf-8")
    route_dict = json.loads(route) 
    lat        = route_dict["latitude"]
    lon        = route_dict["longitude"]
    return lat, lon

def get_device_location(ping) -> int:
    if MODE == 1:
        lat, lon = get_device_latlong(ping)
        locator = Nominatim(user_agent="myGeocoder")
        coordinates = f"{lat}, {lon}"
        location = locator.reverse(coordinates)
        return location.raw["address"]["building"]
    else:
        return random.randint(0, len(LOCATIONS)-1)

class Analysis:
    """
    self.pings     : List[Ping]
    self.density   : List[int]                        # density[location_idx] = number of connected devices connected at location
    self.ratings   : List[List[datetime, int, int]]   # row = [datetime, location_idx, rating])

    self.processed : bool
    self.tick      : int
    self.state     : int                              # STATE_NORMAL or STATE_ERROR

    self.scores
    self.ratings
    """
    STATE_NORMAL = 0
    STATE_EMPTY  = 1
    STATE_ERROR  = 2

    def __init__(self):
        self.pings     = []

        self.processed = True
        self.state     = Analysis.STATE_EMPTY
        self.tick      = 0

        self.ratings   = np.array([])
        self.density   = np.zeros((1,len(LOCATIONS)))
        self.scores    = np.zeros(len(LOCATIONS))

    def update(self, pings, error=False):
        """
        Callback function for ping.py
        """
        if error:
            self.state = Analysis.STATE_ERROR
            self.tick  += 1
            return

        self.pings     = pings
        self.processed = False
        self.state     = Analysis.STATE_NORMAL
        self.tick      += 1

    def score(self, location):
        """
        Gets busyness score for given location
        """
        # TODO - connect to Sachin's
        return 1

    def process(self):
        """
        Processes pings into location densities
        """
        devices = set()
        for ping in self.pings:
            if ping in devices:
                continue
            else:
                devices.add(ping)

            self.density[get_device_location(ping)] += 1

        for location_idx in range(len(LOCATIONS)):
            self.score(location_idx)

        self.processed = True

    def rate_location(self, location, rating):
        """
        Called by front end whenever a user rates a location
        """
        if not isinstance(rating, int) or rating < 1 or rating > 5:
            return

        np.append(self.ratings, [[datetime.datetime.now(), location, rating]], axis=0)
        self.tick += 1
        self.processed = False

    def get_location_scores(self):
        """
        Called by front end to get access to the locations busyness scores
        """
        return self.scores