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

        self.listxs = list(set(self.xs))           #remove the same data from xs,ys,zs
        self.listxs.sort(key=self.xs.index)
        self.listys = list(set(self.ys))
        self.listys.sort(key=self.ys.index)
        self.listzs = list(set(self.zs))
        self.listzs.sort(key=self.zs.index)



        self.distances = [0]*len(self.listxs)              #init data list
        self.end = [0]*(len(self.listxs)-1)
        self.colorx = [0]*(len(self.listxs)-1)
        self.colory = [0]*(len(self.listxs)-1)
        self.colorz = [0]*(len(self.listxs)-1)

        for i in range(0, len(self.listxs)):              #sort circle

            for j in range(0, len(self.listxs)):          #calculate the distance between endpoint and others
                self.distances[j] = math.sqrt((self.listxs[j] - self.endpoint[0]) ** 2 + (self.listys[j] - self.endpoint[1]) ** 2 + (self.listzs[j] - self.endpoint[2]) ** 2)

            self.distances.remove(0.0)                    #remove the distance between end point and endpoint

            if len(self.distances) != 0:
                minpoint = min(self.distances)

            for k in range(0, len(self.distances)):         #get next point position
                if self.distances[k] == minpoint:


                    self.colorx[i] = self.listxs[k]          #store sorted data in colorx,colory,colorz
                    self.colory[i] = self.listys[k]
                    self.colorz[i] = self.listzs[k]
                    #print(self.colorx)

                    self.listxs.remove(self.endpoint[0])      #remove endpoint data for next calculation
                    self.listys.remove(self.endpoint[1])
                    self.listzs.remove(self.endpoint[2])

                    self.endpoint[0] = self.listxs[k]         #update endpoint data for next calculation
                    self.endpoint[1] = self.listys[k]
                    self.endpoint[2] = self.listzs[k]

                    break
                else:
                    continue




    def get_end(self):

        return self.end


    def get_colorx(self):
        return self.colorx

    def get_colory(self):
        return self.colory

    def get_colorz(self):
        return self.colorz