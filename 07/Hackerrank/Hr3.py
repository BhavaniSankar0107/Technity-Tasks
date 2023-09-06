#Staircase
def staircase(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        hashtags = "#" * i
        print(spaces + hashtags)

# Input
n = int(input())

# Print the staircase
staircase(n)