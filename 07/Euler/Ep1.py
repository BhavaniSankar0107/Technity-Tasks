#Multiples of 3 and 5
def sum_of_multiples(n):
    n -= 1  # We want multiples below N, so subtract 1
    sum_of_three = (3 * (n // 3) * ((n // 3) + 1)) // 2
    sum_of_five = (5 * (n // 5) * ((n // 5) + 1)) // 2
    sum_of_fifteen = (15 * (n // 15) * ((n // 15) + 1)) // 2
    total = sum_of_three + sum_of_five - sum_of_fifteen
    return total

# Input
t = int(input())
for i in range(t):
    n = int(input())
    
    # Calculate and print the sum of multiples of 3 or 5 below N
    result = sum_of_multiples(n)
    print(result)
