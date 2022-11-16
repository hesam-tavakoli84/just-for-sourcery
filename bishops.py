def squares(i):
    if (i & 1) == 1:
        return int(i / 4) * 2 + 1
    else:
        return int((i - 1) / 4) * 2 + 2

def placements(n):
    if n > 2 * 8 - 1:
        return 0

    dp = [[0 for i in range(n + 1)]
          for i in range(8 * 2)]

    for i in range(8 * 2):
        dp[i][0] = 1
    dp[1][1] = 1

    for i in range(2, 8 * 2, 1):
        for j in range(1, n + 1, 1):
            dp[i][j] = (dp[i - 2][j] + dp[i - 2][j - 1] * (squares(i) - j + 1))

    ans = 0
    for i in range(0, n + 1, 1):
        ans += (dp[8 * 2 - 1][i] * dp[8 * 2 - 2][n - i])

    return ans

if __name__ == "__main__":
    for n in range(1, 2 * 8 - 1, 2):
        print(f"{n} Bishop(s): ", placements(n))
