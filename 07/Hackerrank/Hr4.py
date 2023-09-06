#Birthday Cake Candles
def birthdayCakeCandles(candles):
    # Find the maximum height of the candles
    max_height = max(candles)
    
    # Count how many candles have the maximum height
    count = candles.count(max_height)
    
    return count

# Input
n = int(input())
candles = list(map(int, input().split()))

# Calculate the number of tallest candles
result = birthdayCakeCandles(candles)

# Output the result
print(result)