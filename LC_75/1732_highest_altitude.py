def largestAltitude(gain):
    max_altitude = 0
    altitude = 0
    for i in range(len(gain)):
        altitude = altitude + gain[i]
        if altitude >= max_altitude:
            max_altitude = altitude
    return max_altitude

gain =[-4,-3,-2,-1,4,3,2]
print(largestAltitude(gain))