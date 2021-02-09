import aprslib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import re


# Map bounding box
range = 'auburn_macon'
if range == 'auburn':
    BBox = ((-85.6110,-84.9712,32.4864,32.7197))
    map_img = plt.imread("map_auburn.png")
elif range == 'auburn_macon':
    BBox = ((-85.6514,-82.8561,32.1011,33.1847))
    map_img = plt.imread("map_auburn_macon.png")
elif range == 'macon':
    BBox = ((-83.7592,-82.4369,32.7313,33.5575))
    map_img = plt.imread("map_macon.png")
else:
    print("Unknown range")

# Using readlines()
file1 = open('aprs-log.txt', 'r')
Lines = file1.readlines()

count = 0
N = len(Lines)
timestamps = np.zeros(N)
latitudes = np.zeros(N)
longitudes = np.zeros(N)
altitudes = np.zeros(N)
speeds = np.zeros(N)
courses = np.zeros(N)
voltages = np.zeros(N)

for line in Lines:
    packet = aprslib.parse(line)
    timestamps[count] = packet['timestamp']
    latitudes[count] = packet['latitude']
    longitudes[count] = packet['longitude']
    altitudes[count] = packet['altitude']
    speeds[count] = packet['speed']
    courses[count] = packet['course']
    voltages[count] = int(re.findall(r'V=(\w+)', packet['comment'])[0])/1000
    dt = datetime.utcfromtimestamp(timestamps[count]).strftime('%Y-%m-%d %H:%M:%S')
    print("%s:\t[Lat,Lon,Alt(m)] = %.6f,%.6f,%.2f\tCourse = %d\tSpeed = %.2f\tV = %.2f\t" % 
    (dt,latitudes[count],longitudes[count],altitudes[count],courses[count],speeds[count],voltages[count]))
    count += 1

# Plot results    
fig,ax = plt.subplots(figsize=(8,4))

ax.scatter(longitudes,latitudes,zorder=1,c='b',s=20)

ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])

ax.imshow(map_img,zorder=0,extent = BBox, aspect='equal')

fig,ax = plt.subplots(2,2)

ax[0,0].plot(altitudes)
ax[0,0].set(xlabel="Index",ylabel="Altitude (m)")
ax[0,0].set_title("Altitude")

ax[1,0].plot(courses)
ax[1,0].set(xlabel="Index",ylabel="Course")
ax[1,0].set_title("GPS Course")

ax[0,1].plot(speeds)
ax[0,1].set(xlabel="Index",ylabel="Speed (m/s)")
ax[0,1].set_title("GPS Speed")

ax[1,1].plot(voltages)
ax[1,1].set(xlabel="Index",ylabel="Voltage (V)")
ax[1,1].set_title("Voltage Levels")

plt.tight_layout()
plt.show()