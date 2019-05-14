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
        #listvertex = list(set(self.vertex))
        #listvertex.sort(key=self.vertex.index)
        self.listxs = list(set(self.xs))
        self.listxs.sort(key=self.xs.index)
        self.listys = list(set(self.ys))
        self.listys.sort(key=self.ys.index)
        self.listzs = list(set(self.zs))
        self.listzs.sort(key=self.zs.index)
        print(len(self.listxs))


        distances = [0]*len(self.listxs)
        self.end = [0]*len(self.listxs)
        self.colorx = [0]*len(self.listxs)
        self.colory = [0]*len(self.listxs)
        self.colorz = [0]*len(self.listxs)

        for i in range(0, len(self.listxs)):
            for j in range(0, len(self.listxs)):
                distances[j] = math.sqrt((self.listxs[j] - self.endpoint[0]) ** 2 + (self.listys[j] - self.endpoint[1]) ** 2 + (self.listzs[j] - self.endpoint[2]) ** 2)
            print(distances)
            print(len(distances))
            distances.remove(0.0)

            #print(self.endpoint[0])
            #print(self.endpoint[1])
            #print(self.endpoint[2])
            minpoint = min(distances)

            for k in range(0, len(distances)):
                if distances[k] == minpoint:
                    #self.end[i] = self.listvertex[k]
                    print(minpoint)
                    print(distances[k])

                    self.colorx[i] = self.listxs[k]
                    self.colory[i] = self.listys[k]
                    self.colorz[i] = self.listzs[k]
                    print(self.endpoint[0])
                    print(k)
                    print(self.listxs[k])
                    print(self.end)
                    self.endpoint[0] = self.listxs[k]
                    self.endpoint[1] = self.listys[k]
                    self.endpoint[2] = self.listzs[k]
                    print(self.endpoint[0])

                    self.listxs.remove(self.listxs[k])
                    self.listys.remove(self.listys[k])
                    self.listzs.remove(self.listzs[k])

        #print(self.end)

    def get_end(self):
        return self.end

    def get_colorx(self):
        return self.colorx

    def get_colory(self):
        return self.colory

    def get_colorz(self):
        return self.colorz