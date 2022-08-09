import numpy.polynomial.polynomial as poly

p1 = [1, 1, -1]
p2 = [2, 0, 0, 1]

p = poly.polymul(p1, p2)

print(p);

r = poly.polyroots(p)
print(r)

x=2
px = poly.polyval(x, p)
print(px)