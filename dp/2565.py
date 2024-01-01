n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]
rs = [1] * n
nums.sort()

for i in range(n):
    for j in range(i):
        if nums[i][1] > nums[j][1]:
            rs[i] = max(rs[i], rs[j]+1)


print(n-max(rs))