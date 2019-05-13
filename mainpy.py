from data import Dataimport
from coordinates import Coordinatesimport
from endpoint import Endpointcalculation
from Sort import pointsort
from colorplt import colorfigure

a = Dataimport("data/centerline.csv")
b = Coordinatesimport(a.get_xs(), a.get_ys(), a.get_zs())
c = Endpointcalculation(a.get_xs(), a.get_ys(), a.get_zs())
d = pointsort(c.endpoint(c.enddistance(), c.comparsion(c.enddistance())), a.get_vertex(), a.get_xs(), a.get_ys(), a.get_zs())
e = colorfigure(d.get_colorx(), d.get_colory(), d.get_colorz())

#for i range(0, len(d.get_colorx()))

b.plot('green', 'o')