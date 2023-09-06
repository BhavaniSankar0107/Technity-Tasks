# Compare the triplets
def compareTriplets(a, b):
    alice_score = 0
    bob_score = 0
    
    for i in range(3):
        if a[i] > b[i]:
            alice_score += 1
        elif a[i] < b[i]:
            bob_score += 1
    
    return alice_score, bob_score

# Input
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Calculate comparison points
result = compareTriplets(a, b)

# Output the result
print(result[0], result[1])