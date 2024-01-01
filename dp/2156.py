n = int(input())
wines = [int(input()) for _ in range(n)]

dp = [0] * n

dp[0] = wines[0]
# if 문은 인덱스 에러 방지 위함
if n>1:
    dp[1] = wines[0] + wines[1]
if n>2:
    dp[2] = max(wines[0] + wines[2], wines[1] + wines[2], dp[1]) # 중간것 제외 / 처음 제외 / 마지막 제외(1번째까지의 합)


for i in range(3,n):
    dp[i] = max(dp[i-3] + wines[i-1] + wines[i], dp[i-2] + wines[i], dp[i-1])

# print(dp)
print(max(dp))



