# 숫자 조합
n,k = map(int, input().split())
dp =[[0] * (n+1) for _ in range(k)]

for i in range(k): # k개 이용하여
    for j in range(n+1): # n만들어가기
        if i==0: # 인덱스라 0으로 표기했지만 k==1인 경우를 의미
            dp[i][j] = 1 # n을 1개로 만들때는 n 1가지만 가능
        elif j==0:
            dp[i][j] = 1 # 0을 만들때는 0, 0+0, 0+0+0 등 1가지만 가능
        else:
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000 # 점화식


print(dp[k-1][n])




