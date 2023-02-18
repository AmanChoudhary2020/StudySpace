from typing import Tuple
from flask import Flask
import numpy as np
import datetime

# TODO - list
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

def time_dropoff(dt : datetime.datetime) -> float:
    MIN_TIME = 20
    MAX_TIME = 120

    cur_dt = datetime.datetime.now()
    time_diff = (cur_dt - dt).total_seconds() / 60
    return np.clip(1 - (time_diff - MIN_TIME) / MAX_TIME, 0, 1)

class Analysis:
    """
    self.pings     : List[Ping]
    self.density   : List[int]
        # density[location_idx] = number of connected devices connected at location
    self.ratings   : List[List[datetime, int, int]] 
        # row = [datetime, location_idx, rating])
    self.processed : bool
    self.state     : int
        # STATE_NORMAL or STATE_ERROR

    # TODO - move to database
    self.scores
    self.ratings
    """
    STATE_NORMAL = 0
    STATE_ERROR  = 1

    def __init__(self):
        self.pings     = []
        self.density   = [0] * LOCATIONS
        self.processed = True
        self.state     = Analysis.STATE_ERROR

        self.ratings   = []
        self.scores    = [-1] * LOCATIONS 

    def update(self, pings):
        """
        Callback function for ping.py
        """
        self.pings     = pings
        self.processed = False
        self.state     = Analysis.STATE_NORMAL

    def score(self, location):
        """
        Gets busyness score for given location
        """
        COEFF_CROWDSOURCE = 1
        COEFF_DEVICES     = 1

        # TODO - implement

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
        self.ratings.append([datetime.datetime.now(), location, rating])