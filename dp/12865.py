n,k = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]
nums.sort()

dp = [[0]*(k+1) for _ in range(n+1)]


for i in range(1, n+1):
    for j in range(k+1):
        if j < nums[i-1][0]:
            dp[i][j] = dp[i-1][j]
        if j >= nums[i-1][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-nums[i-1][0]] + nums[i-1][1])

print(dp)
print(dp[n][k])
