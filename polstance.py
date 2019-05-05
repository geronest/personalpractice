import numpy as np

def func1(x, l): return x
def func2(x, l): return (-1/(x + 1e-6) + 1/l)

def interact(i1, i2, len_world, coef = 0.01, func = func2):
    midx = (i1.x + i2.x) / 2.
    midy = (i1.y + i2.y) / 2.
    dis = np.sqrt((i1.x - i2.x)**2 + (i1.y - i2.y)**2)
    i1.x += coef * func(i2.x - i1.x, len_world[0]) / len_world[0]
    i1.y += coef * func(i2.y - i1.y, len_world[1]) / len_world[1]
    i2.x += coef * func(i1.x - i2.x, len_world[0]) / len_world[0]
    i2.y += coef * func(i1.y - i2.y, len_world[1]) / len_world[1]
    
    

#class Indiv(Object):
class Indiv:
    def __init__(self, coo_world):
        self.x = np.random.uniform(coo_world[0], coo_world[1], 1)[0]
        self.y = np.random.uniform(coo_world[2], coo_world[3], 1)[0]
       
    
        
    