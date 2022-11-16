def squares(i):
    return int(i / 4) * 2 + 1 if (i & 1) == 1 else int((i - 1) / 4) * 2 + 2

def placements(n):
    if n > 2 * 8 - 1:
        return 0

    dp = [[0 for _ in range(n + 1)] for _ in range(8 * 2)]

    for i in range(8 * 2):
        dp[i][0] = 1
    dp[1][1] = 1

    for i in range(2, 8 * 2):
        for j in range(1, n + 1):
            dp[i][j] = (dp[i - 2][j] + dp[i - 2][j - 1] * (squares(i) - j + 1))

    return sum((dp[8 * 2 - 1][i] * dp[8 * 2 - 2][n - i]) for i in range(n + 1))

if __name__ == "__main__":
    for n in range(1, 2 * 8 - 1, 2):
        print(f"{n} Bishop(s): ", placements(n))
