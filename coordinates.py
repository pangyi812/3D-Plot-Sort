# draw plot based on the x,y,z vertex data

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

class Coordinatesimport:

    def __init__(self, xs, ys, zs):    # get data from csv data files
        self.xs = xs
        self.ys = ys
        self.zs = zs

    def plot(self, color, mark):     #normal figure
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(self.xs, self.ys, self.zs, c = color, marker = mark)
        ax.set_xlabel('X Lable')
        ax.set_ylabel('Y Lable')
        ax.set_zlabel('Z Lable')
        plt.show()



