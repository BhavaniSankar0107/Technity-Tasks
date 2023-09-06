#Largest Prime Factor
import math

def largest_prime_factor(n):
    # Divide n by 2 until it is odd
    while n % 2 == 0:
        n //= 2
    
    # Now n is guaranteed to be odd
    max_prime = -1
    
    # Check for prime factors up to the square root of n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            max_prime = i
            n //= i
    
    # If n is still greater than 1, it's a prime number itself
    if n > 1:
        max_prime = n
    
    return max_prime

# Input
t = int(input())
for i in range(t):
    n = int(input())
    
    # Calculate and print the largest prime factor of N
    result = largest_prime_factor(n)
    print(result)