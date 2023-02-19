# Location,Rating,Time,Devices
# Union,4,14,50
# Union,3,14,70
# Union,2,14,80
# LSA,4,14,50
# LSA,4,14,50
# LSA,4,14,50

import random
import numpy

final = "Location,Rating,Time,Devices\n"

def generateRandomLog(place, c):
    global final

    log = place
    randTime = random.randint(0, 24)
    
    busyMetric = (min(abs(18-randTime), abs(12-randTime)))/12
    # if busyMetric (0-1) is low, close to a busy time -> low rating

    randRating = 2*c + busyMetric*random.randint(1, 5)
    randDevices = busyMetric*random.randint(10, 1000)
    if randRating < 1:
        randRating += random.randint(1, 3)
    if randRating > 5:
        randRating = 5
    

    log += "," + str(randRating) + "," + str(randTime) + "," + str(randDevices) + "\n"
    final += log


places = ["Hatcher", "Union", "UgLi", "SKB", "Fishbowl", "League", "LSA", "Ross", "IM"]

for i in range(len(places)):
    c = (len(places)-i)/len(places)
    for a in range(1000):
        generateRandomLog(places[i], c)

f = open("data.csv", "w")
f.write(final)
f.close()