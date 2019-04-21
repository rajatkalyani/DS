from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure()

ax1 = fig.add_subplot(111, projection = '3d')

x = [1,2,3,4,5,6,7,8,9,10]
y = [5,3,2,5,6,2,2,1,6,7]
z = [6,2,5,7,9,0,2,2,1,5]

x2 = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
y2 = [-5,-3,-2,-5,-6,-2,-2,-1,-6,-7]
z2 = [6,2,5,7,9,0,2,2,1,5]

ax1.scatter(x, y, z, c='r', marker='o', label='red')
ax1.scatter(x2, y2, z2, c='g', marker='o', label='green')


ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')
plt.legend()
plt.show()
