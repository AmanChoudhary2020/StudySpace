from typing import Tuple
import numpy as np
import datetime

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

# TODO - list out all locations
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
    """
    Determines strength to downgrade importance of crowdsourced score by elapsed time
    """
    MIN_TIME = 20
    MAX_TIME = 120

    cur_dt = datetime.datetime.now()
    time_diff = (cur_dt - dt).total_seconds() / 60
    return np.clip(1 - (time_diff - MIN_TIME) / MAX_TIME, 0, 1)

class Analysis:
    """
    self.pings     : List[Ping]
    self.density   : List[int]                        # density[location_idx] = number of connected devices connected at location
    self.ratings   : List[List[datetime, int, int]]   # row = [datetime, location_idx, rating])

    self.processed : bool
    self.tick      : int
    self.state     : int                              # STATE_NORMAL or STATE_ERROR

    # TODO - move to database
    self.scores
    self.ratings
    """
    STATE_NORMAL = 0
    STATE_EMPTY  = 1
    STATE_ERROR  = 2

    def __init__(self):
        self.pings     = []
        self.density   = [0] * LOCATIONS

        self.processed = True
        self.state     = Analysis.STATE_EMPTY
        self.tick      = 0

        self.ratings   = []
        self.scores    = [-1] * LOCATIONS 

    def update(self, pings, error=False):
        """
        Callback function for ping.py
        """
        if error:
            self.state = Analysis.STATE_ERROR
            self.tick  += 1
            return

        # TODO - add handling for Error state
        self.pings     = pings
        self.processed = False
        self.state     = Analysis.STATE_NORMAL
        self.tick      += 1

    def score(self, location):
        """
        Gets busyness score for given location
        """
        COEFF_CROWDSOURCE = 1
        COEFF_DEVICES     = 0

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

        for location_idx in range(len(LOCATIONS)):
            self.score(location_idx)

        self.processed = True

    def rate_location(self, location, rating):
        """
        Called by front end whenever a user rates a location
        """
        # TODO - convert location to location_idx
        # TODO - verify score is from 1 to 5
        self.ratings.append([datetime.datetime.now(), location, rating])
        self.tick += 1
        self.processed = False

    def get_location_scores(self):
        """
        Called by front end to get access to the locations busyness scores
        """
        return self.scores