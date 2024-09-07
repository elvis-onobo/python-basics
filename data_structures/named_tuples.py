from collections import namedtuple

# named tuples creates more readable code
Point = namedtuple('Point', ['x', 'y', 'z'])
p = Point(0,1,2)
print(p.x, p.y, p.z)


Letters = namedtuple('Letters', ['a', 'b', 'c'])
l = Letters(a='apple', b='ball', c='cat')
print(l.a, l.b, l.c)