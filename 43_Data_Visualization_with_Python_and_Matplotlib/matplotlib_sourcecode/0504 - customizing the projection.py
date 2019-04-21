from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

m = Basemap(projection='mill',
            llcrnrlat = -40,
            llcrnrlon = -40,
            urcrnrlat = 50,
            urcrnrlon = 75,
            resolution = 'l')

m.drawcoastlines()
m.fillcontinents()
m.drawmapboundary()

plt.title('Basemap Example with Title')
plt.show()
