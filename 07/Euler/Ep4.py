#Largest Palindrome Product
def largest_palindrome_product(n):
    for palindrome in range(n - 1, 100000, -1):
        if str(palindrome) == str(palindrome)[::-1]:
            for factor in range(999, 99, -1):
                if palindrome % factor == 0:
                    quotient = palindrome // factor
                    if 99 < quotient < 1000:
                        return palindrome

# Input
t = int(input())
for i in range(t):
    n = int(input())
    
    # Calculate and print the largest palindrome product
    result = largest_palindrome_product(n)
    print(result)