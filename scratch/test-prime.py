import math

print "Enter a number to find its factors:"
N = int(raw_input())

i = 1

while i <= math.sqrt(N):
    if N % i == 0:
        print "It is divisible by", i, "and", N / i
    i=i+1

print "We are done!"
        
    
    

        