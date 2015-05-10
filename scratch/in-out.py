import math

print "Enter the first triangle side:"
a = int(raw_input())

print "Enter the second triangle side:"
b = int(raw_input())

a_squared = a * a
b_squared = b * b
c_squared = a_squared + b_squared

print "The hypotenuse", math.sqrt(c_squared)