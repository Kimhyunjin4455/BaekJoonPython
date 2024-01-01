# n가지의 동전, 합이 k원이 되도록하는 경우의 수(동전은 중복 사용 가능)
N,K = map(int, input().split())
nums = [int(input()) for _ in range(N)]
dp = [0] * (K+1)
dp[0] = 1

for i in range(len(nums)):
    for j in range(nums[i], K+1): # 최대 반복수는 최대 금액때까지
        dp[j] = dp[j] + dp[j - nums[i]]

print(dp[K])







