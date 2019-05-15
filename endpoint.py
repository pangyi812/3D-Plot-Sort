import math

class Endpointcalculation:           #init program
    def __init__(self, xs_=[], ys_=[], zs_=[]):
        self.xs = xs_
        self.ys = ys_
        self.zs = zs_
        self.enddistance()
        self.comparsion(self.enddistance())
        self.endpoint(self.enddistance(), self.comparsion(self.enddistance()))

    def enddistance(self):            #calculate distance between every point with other points
        distancepoint = [0]*len(self.xs)
        sum = []
        point = []

        for i in range(0, len(self.xs)):
            sum.append(0)
            for j in range(0, len(self.xs)):
                 distancepoint[j] = math.sqrt((self.xs[i] - self.xs[j])**2+(self.ys[i] - self.ys[j])**2 + (self.zs[i]-self.zs[j])**2)
                 sum[i] = sum[i] + distancepoint[j]
        point.extend(sum)

        return point     #get distance result with other points

    def comparsion(self, point=[]):   #get biggest distance
        mark = max(point)

        return mark

    def endpoint(self, point=[], mark=0):   #get biggest distances reference to the point
        endpoint = []
        for i in range(0, len(point)):
            if point[i] == mark:
                endpoint.append(self.xs[i])
                endpoint.append(self.ys[i])
                endpoint.append(self.zs[i])

        return endpoint                       #get end point






