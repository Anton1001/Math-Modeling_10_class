import math
t=200
e=300
k=1.38*10**23
E=2.718
h=6.6210**(-34)
N=(2/((math.pi)**0.5))*(h/((k*t)**1.5))*((E**(-e/k*t))*(e**(t/2)))
print(N)