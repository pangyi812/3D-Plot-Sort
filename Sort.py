import math
import numpy
class pointsort:

    def __init__(self, endpoint=[], vertex=[],  xs_=[], ys_=[], zs_=[]):
        self.endpoint = endpoint
        self.vertex = vertex
        self.xs = xs_
        self.ys = ys_
        self.zs = zs_
        self.pointsorts(self.sort(), self.colorsort(self.sort()))


    def sort(self):
        distances = [0]*len(self.xs)

        for i in range(0, len(self.xs)):
             distances[i] = math.sqrt((self.xs[i] - self.endpoint[0]) ** 2 + (self.ys[i] - self.endpoint[1]) ** 2 + (self.zs[i] - self.endpoint[2]) ** 2)
            #print(distances)
        return distances

    def colorsort(self, endsort=[], distances=[]):
        endsort.append(distances)

        for i in range(0, len(self.xs)):

            for j in range(0, len(self.xs)-1):
                if endsort[j] > endsort[j + 1]:
                    bridge = endsort[j+1]
                    endsort[j+1] = endsort[j]
                    endsort[j] = bridge

        return endsort

    def pointsorts(self, distances=[], endsort=[]):
        pointsort = [0] * len(self.xs)
        self.colorx = [0] * len(self.xs)
        self.colory = [0] * len(self.xs)
        self.colorz = [0] * len(self.xs)

        for i in range(0, len(self.xs)):
            for j in range(0, len(self.xs)-1):
                if distances[j] == endsort[i]:
                    pointsort[i] = self.vertex[j]
                    self.colorx[i] = self.xs[j]
                    self.colory[i] = self.ys[j]
                    self.colorz[i] = self.zs[j]
        print(pointsort)
        return pointsort

    def get_colorx(self):
        return self.colorx

    def get_colory(self):
        return self.colory

    def get_colorz(self):
        return self.colorz