import math
import numpy
class pointsort:

    def __init__(self, endpoint=[], vertex=[],  xs_=[], ys_=[], zs_=[]):
        self.endpoint = endpoint
        self.vertex = vertex
        self.xs = xs_
        self.ys = ys_
        self.zs = zs_
        self.sort()


    def sort(self):
        distances = [0]*len(self.xs)
        self.end = [0]*len(self.xs)
        self.colorx = [0]*len(self.xs)
        self.colory = [0]*len(self.xs)
        self.colorz = [0]*len(self.zs)

        for i in range(0, len(self.xs)):
            for j in range(0, len(self.xs)):
                distances[j] = math.sqrt((self.xs[j] - self.endpoint[0]) ** 2 + (self.ys[j] - self.endpoint[1]) ** 2 + (self.zs[j] - self.endpoint[2]) ** 2)
            print(distances)
            print(len(distances))
            list1 = list(set(distances))
            list1.sort(key=distances.index)
            list1.remove(0.0)

            print(list1)
            print(len(list1))
            #print(self.endpoint[0])
            #print(self.endpoint[1])
            #print(self.endpoint[2])
            minpoint = min(list1)

            for k in range(0, len(distances)):
                if distances[k] == minpoint:
                    self.end[i] = self.vertex[k]
                    print(minpoint)
                    print(distances[k])

                    self.colorx[i] = self.xs[k]
                    self.colory[i] = self.ys[k]
                    self.colorz[i] = self.zs[k]
                    print(self.endpoint[0])
                    print(k)
                    print(self.xs[k])
                    self.endpoint[0] = self.xs[k]
                    self.endpoint[1] = self.ys[k]
                    self.endpoint[2] = self.zs[k]
                    print(self.endpoint[0])

                    self.xs.remove(self.xs[k])
                    self.ys.remove(self.ys[k])
                    self.zs.remove(self.zs[k])

        #print(self.end)

    def get_end(self):
        return self.end

    def get_colorx(self):
        return self.colorx

    def get_colory(self):
        return self.colory

    def get_colorz(self):
        return self.colorz