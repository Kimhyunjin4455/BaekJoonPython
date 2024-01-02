# word1 = input()
# word2 = input()
# word3 = input()
#
# l1 = len(word1)
# l2 = len(word2)
# l3 = len(word3)
#
# dp = [[[0]*(l3+1) for _ in range(l2+1)] for _ in range(l1+1)]
#
# for i in range(1,l1+1):
#     for j in range(1,l2+1):
#         for k in range(1,l3+1):
#             if word1[i-1] == word2[j-1] == word3[k-1]:
#                 dp[i][j][k] = dp[i-1][j-1][k-1]+1
#             else:
#                 dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
#
# print(dp[-1][-1][-1])
#
#


word1 = input()
word2 = input()
word3 = input()

l1 = len(word1)
l2 = len(word2)
l3 = len(word3)


dp = [[[0] * (l3+1) for _ in range(l2+1)] for _ in range(l1+1)]                 # 0부터 l1(l2,l3)까지의 인덱스가 필요하기에 +1

# 이전 값을 이용
for i in range(1,l1+1):                                                         # 이전 값을 이용하기에 반복문의 범위 1~n+1
    for j in range(1,l2+1):
        for k in range(1,l3+1):
            if word1[i-1] == word2[j-1] == word3[k-1]:                          # 문자의 값이 같다면 (인덱스0부터)
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1                             # 같기 전의 값 + 1
            else:                                                               # 문자의 값이 다르다면
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])  # 이전까지의 값들 중 최댓값


print(dp)
print(dp[-1][-1][-1])