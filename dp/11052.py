# 8가지의 등급
# 카드팩의 종류 n가
n = int(input())
cards = list(map(int, input().split()))
dp = [0] * 10001 # 10001로 변경시키



for i in range(1,n+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i], dp[i-j] + cards[j-1])

print(max(dp))




