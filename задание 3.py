from conctant import m,g,h,v
import numpy as np
def energy(m,h,v):
    F=(m*v**2)/2+m*g*h
    return(F)
print (energy(m,h,v))    