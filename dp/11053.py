# N = int(input())
# nums = list(map(int, input().split()))
# rs = [1] * (N)
#
#
# for i in range(N):
#     for j in range(i):
#         if nums[i] > nums[j]:
#             rs[i] = max(rs[i], rs[j]+1)
#
#
# print(max(rs))

n = int(input())
nums = list(map(int, input().split()))
dp = [1] * n

for i in range(len(nums)):
    for j in range(i):
        if nums[i]>nums[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))