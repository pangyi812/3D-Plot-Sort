import math

class pointsort:

    def sort(self):
        distances = []
        i, j = int()

        for i in range(1, 298):
            for row in get_vertex:
                distances[i] = math.sqrt(int(xs(i) - row(0)) ** 2 + int(ys(i) - row(1)) ** 2 + int(zs(i) - row(2)) ** 2)

    def colorsort(self):
        endsort = []
        endsort.append(distances)

        for i in range(1, 298):
            for j in range(1, 299-i):
                if endsort[j] > endsort[j + 1]:
                    self.endsort[j+1], self.endsort[j] = self.endsort[j], self.endsort[j+1]
        return self.endsort

    def pointsorts(self):
        pointsort = []

        for i in range(1, 298):
            for j in range(1, 298):
                if pointsort[i] == distance[j]:
                    pointsort[i] = vertex[j]
        return self.pointsort