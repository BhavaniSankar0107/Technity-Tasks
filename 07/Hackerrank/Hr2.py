# Diagonal Difference
def diagonalDifference(arr):
    left_diagonal_sum = 0
    right_diagonal_sum = 0
    n = len(arr)

    for i in range(n):
        left_diagonal_sum += arr[i][i]
        right_diagonal_sum += arr[i][n - 1 - i]

    return abs(left_diagonal_sum - right_diagonal_sum)

# Input
n = int(input())
matrix = []
for j in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Calculate diagonal difference
result = diagonalDifference(matrix)

# Output the result
print(result)