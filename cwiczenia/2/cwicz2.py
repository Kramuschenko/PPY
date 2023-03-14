import math

a = b = 2566
a = 2566
b = a

print(id(a), id(b))

b = 4000

print(id(a), id(b))
print(type(a))

print(type("ujyadfs"))
print(type(False))
print(type(44.0))

a,b,c,d,e = 1.5,2.5,3.5,4.5,5.5
print(a+b+c+d+e)
print(round(a)+round(b)+round(c)+round(d)+round(e))
print(int(a)+int(b)+int(c)+int(d)+int(e))
print(math.ceil(a)+math.ceil(b)+math.ceil(c)+math.ceil(d)+math.ceil(e))