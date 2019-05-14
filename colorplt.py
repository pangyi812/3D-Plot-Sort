# draw plot based on the x,y,z vertex data

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

class colorfigure:

    def __init__(self, colorx, colory, colorz):
        self.xs = colorx
        self.ys = colory
        self.zs = colorz

    def plot(self, mark):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        c = list(range(1, len(self.xs)))
        ax.scatter(self.xs, self.ys, self.zs, c, marker=mark)
        ax.set_xlabel('X Lable')
        ax.set_ylabel('Y Lable')
        ax.set_zlabel('Z Lable')
        plt.show()
