# draw plot based on the x,y,z vertex data

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

class colorfigure:

    def __init__(self, colorx, colory, colorz):    #input x,y,z position data
        self.xs = colorx
        self.ys = colory
        self.zs = colorz
        self.plot('o')

    def plot(self, mark):                          #get color plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        k = list(range(1, len(self.xs)+1))

        ax.scatter(self.xs, self.ys, self.zs, c=k, cmap=plt.cm.hot, marker=mark)

        ax.set_xlabel('X Lable')
        ax.set_ylabel('Y Lable')
        ax.set_zlabel('Z Lable')
        plt.show()
