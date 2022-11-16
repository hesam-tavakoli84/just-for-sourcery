# Gorbe just GOD!

n = int(input())
input()
states = []
moves = list(map(int, input().split()))

for i in range(n):
    print(f"{i}: ", end="")

    win = any(i - k >= 0 and states[i - k] == "L" for k in moves)
    state = "W" if win else "L"
    states.append(state)
    print(state)

