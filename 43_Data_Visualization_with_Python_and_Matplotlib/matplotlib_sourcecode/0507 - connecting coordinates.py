from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

m = Basemap(projection='mill',
            llcrnrlat = 25,
            llcrnrlon = -130,
            urcrnrlat = 50,
            urcrnrlon = -60,
            resolution = 'l')

m.drawcoastlines()
m.drawcountries(linewidth=2)
m.drawstates(color='black')

xs = []
ys = []

# 29 north 95 west
# NYC
hlat, hlon = 40.7127, -74.0059
xpt, ypt = m(hlon, hlat)
xs.append(xpt)
ys.append(ypt)
m.plot(xpt, ypt, 'r*', markersize=15)


# LA, CA
blat, blon = 34.05, -118.25
xpt, ypt = m(blon, blat)
xs.append(xpt)
ys.append(ypt)
m.plot(xpt, ypt, 'bo')

land_check = m.is_land(xpt, ypt)
print(land_check)

m.plot(xs, ys, 'r', linewidth=2, label='Flight 115')

m.drawgreatcircle(hlon, hlat, blon, blat, linewidth=2, color='c', label='Great circle')


plt.legend(loc=4)
plt.title('Basemap Example with Title')
plt.show()



















