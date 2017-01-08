from pyexplr import pyexplr

objects = ['object no {}'.format(i) for i in range(20)]
objects[0] = [0, 1, 2]
objects[10] = ['this', 'is', 'inner', list, 1]
objects[11] = ['this', 'is', 'inner', list, 1]

pyexplr(objects)