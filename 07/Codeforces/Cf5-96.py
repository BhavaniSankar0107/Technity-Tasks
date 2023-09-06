player_string = input()

consecutive_count = 1
dangerous = False

for i in range(1, len(player_string)):
    if player_string[i] == player_string[i - 1]:
        consecutive_count += 1
        if consecutive_count >= 7:
            dangerous = True
            break

    else:
        consecutive_count = 1

if dangerous:
    print("YES")
else:
    print("NO")