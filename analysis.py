from typing import Tuple
from flask import Flask
import datetime

LOCATIONS = [
    "Union",
    "UGLI"
]

def get_device_id(ping) -> int:
    pass

def get_device_latlong(ping) -> Tuple[int, int]:
    pass

def get_device_location(ping) -> int:
    lat, long = get_device_latlong(ping)
    # TODO - implement

class Analysis:
    """
    self.pings     : List[Ping]
    self.density   : List[int]
        # density[location_idx] = number of connected devices connected at location
    self.processed : bool
    self.ratings   : List[List[datetime, int, int]] 
        # row = [datetime, location_idx, rating])
    self.state     : int
        # STATE_NORMAL or STATE_ERROR
    """
    STATE_NORMAL = 0
    STATE_ERROR  = 1

    def __init__(self):
        self.pings     = []
        self.density   = [0] * LOCATIONS
        self.processed = True
        self.ratings   = []
        self.state     = Analysis.STATE_ERROR

    def update(self, pings):
        """
        Callback function for ping.py
        """
        self.pings     = pings
        self.processed = False
        self.state     = Analysis.STATE_NORMAL

    def score(self, location):
        """
        Produces a score
        """

    def process(self):
        """
        Processes pings into location densities
        """
        devices = set()
        for ping in self.pings:
            did = get_device_id(ping)
            if did in devices:
                continue
            else:
                devices.add(did)

            self.density[get_device_location(ping)] += 1

    def rate_location(self, location, rating):
        """
        Called by front end whenever a user rates a location
        """
        self.ratings.append([datetime.now(), location, rating])