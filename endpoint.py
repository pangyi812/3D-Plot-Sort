import math

class Endpointcalculation:
    def __init__(self, xs, ys, zs):
        self.xs = xs
        self.ys = ys
        self.zs = zs

    def enddistance(self):
        distancepoint = []
        sum = []
        point = []
        i, j = int()

        for i in (1, 298):
             for j in range(i+1, 298):
                distancepoint[j] = math.sqrt(int(xs(i) - xs(j))**2+int(ys(i) - ys(j))**2 + int(zs(i)-zs(j))**2)
             sum[i] = sum(distancepoint[j])
        point.append(sum)

    def comparsion(self):
        mark = point[1]
        for i in range(1, 298):
            if mark < point[i+1]:
                mark = point[i+1]
        return self.mark

    def endpoint(self):
        endpoint = []
        for i in range(1, 298):
            if point[i] == mark:
                self.endpoint[0].append(xs(i))
                self.endpoint[1].append(ys(i))
                self.endpoint[2].append(zs(i))
        return endpoint






