n = int(input())
nums = [int(input()) for _ in range(n)]
dp = [0] * n

if n==1:
    print(nums[0])
    exit()
elif n==2:
    print(nums[0] + nums[1])
    exit()

dp[0] = nums[0]
dp[1] = nums[0] + nums[1]
dp[2] = max(nums[1] + nums[2], nums[0] + nums[2])
for i in range(3,n):
    dp[i] = max(nums[i] +nums[i-1] +dp[i-3], nums[i] + dp[i-2])
print(dp[-1])

# dp[-1] 대신 max(dp)는 틀림
# 반례
#4
#1
#1000
#10
#1 일 경우 최댓값은 1010 이지만 답은 1002 -> 마지막 칸을 밟지 못했기 때문.(문제 조건: 마지막 계단을 반드시 밟기)