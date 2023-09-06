n = int(input())

results = []

for i in range(n):
    word = input()
    if len(word) > 10:
        abbreviated_word = word[0] + str(len(word) - 2) + word[-1]
        results.append(abbreviated_word)
    else:
        results.append(word)

for result in results:
    print(result)