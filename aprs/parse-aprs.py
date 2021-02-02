import aprslib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Map bounding box
BBox = ((-86.1575,-83.5620,31.2410,33.0800))
map_img = plt.imread("map.png")

# Using readlines()
file1 = open('log.txt', 'r')
Lines = file1.readlines()

count = 0
N = len(Lines)
latitudes = np.zeros(N)
longitudes = np.zeros(N)
altitudes = np.zeros(N)

for line in Lines:
    packet = aprslib.parse(line)
    latitudes[count] = packet['latitude']
    longitudes[count] = packet['longitude']
    altitudes[count] = packet['altitude']
    print("(Lat,Lon,Alt) = %.6f,%.6f,%.2f" % (latitudes[count],longitudes[count],altitudes[count]))
    count += 1

# Plot results    
fig,ax = plt.subplots(figsize=(8,6))

ax.scatter(longitudes,latitudes,zorder=1,alpha=0.2,c='b',s=10)

ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])

ax.imshow(map_img,zorder=0,extent = BBox, aspect='equal')

fig,ax = plt.subplots(figsize=(8,4))
ax.plot(altitudes)

ax.set(xlabel="Index",ylabel="Altitude (m)")
plt.tight_layout()
plt.show()