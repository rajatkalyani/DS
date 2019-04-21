from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

m = Basemap(projection='mill',
            llcrnrlat = 20,
            llcrnrlon = -130,
            urcrnrlat = 50,
            urcrnrlon = -60,
            resolution = 'l')

m.drawcoastlines()
m.drawcountries(linewidth=2)
m.drawstates(color='black')

# 29 north 95 west
# Houston, TX
lat, lon = 29.7604, -95.3698
xpt, ypt = m(lon, lat)
m.plot(xpt, ypt, 'r*', markersize=15)

# Boulder, CO
lat, lon = 40.125, -104.237
xpt, ypt = m(lon, lat)
m.plot(xpt, ypt, 'bo')

land_check = m.is_land(xpt, ypt)

print(land_check)


plt.title('Basemap Example with Title')
plt.show()
