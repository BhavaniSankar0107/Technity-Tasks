#Smallest Multiple
import math

def smallest_multiple(n):
    lcm = 1
    for i in range(2, n + 1):
        lcm = (lcm * i) // math.gcd(lcm, i)
    return lcm

# Input
t = int(input())
for i in range(t):
    n = int(input())
    
    # Calculate and print the smallest multiple
    result = smallest_multiple(n)
    print(result)