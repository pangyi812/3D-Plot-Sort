from data import Dataimport
from coordinates import Coordinatesimport

a = Dataimport("data/centerline.csv")
b = Coordinatesimport(a.get_xs(), a.get_ys(), a.get_zs())
b.plot('red', 'o')