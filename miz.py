# Gorbe just GOD!

n = int(input())
input()
states = []
moves = list(map(int, input().split()))

for i in range(n):
    win = False
    print(f"{i}: ", end="")

    for k in moves:
        if i - k >= 0 and states[i - k] == "L":
            win = True
            break

    state = "W" if win else "L"
    states.append(state)
    print(state)

