#Even Fibonacci Numbers
def sum_even_fibonacci(n):
    a, b = 1, 2
    total = 0
    while a <= n:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    return total

# Input
t = int(input())
for i in range(t):
    n = int(input())
    
    # Calculate and print the sum of even-valued Fibonacci terms not exceeding N
    result = sum_even_fibonacci(n)
    print(result)