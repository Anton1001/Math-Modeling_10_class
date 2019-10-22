import math
g=10
h=100
a=math.pi/3
b=math.radians(30)
v=(g*h*(1/math.tan(b))**2)/(2*math.cos(a)**2)*(1-(1/math.tan(b))*(1/math.tan(a)))
print(v)



