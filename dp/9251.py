# LCS
# 두 문자열
words1 = input()
words2 = input()

l1 = len(words1)
l2 = len(words2)
dp = [[0] * (l2+1) for _ in range(l1+1)]                # 이전 값을 갖고 하기 때문에 글자의 크기보다 1 크게

#dp = [0] * max(l1,l2)

# for i in range(l2):
#     cnt = 0
#     for j in range(l1):
#         # 첫번째 문자열에 대해 두번째 문자열의 문자가 하나씩 반복적용돰
#         if cnt < dp[j]:
#             cnt = dp[j] # 글자가 다른 경우 => 누적값이 해당 위치의 값보다 작다면 해당 위치의 값으로 교체
#         elif words1[j] == words2[i]: # 순회하면서 만나는 문자열이 같다면
#             dp[j] = cnt + 1 # 이전까지의 최댓값 +1
#     print(dp)
# print(max(dp))

for i in range(1,l1+1):                                 # 이전 값을 갖고 하기 때문에 글자의 크기보다 1 크게
    for j in range(1,l2+1):
        if words1[i-1] == words2[j-1]:                  # 두 문자가 같다면
            dp[i][j] = dp[i-1][j-1]+1                   # 이전 문자까지의 길이 + 1 (글자를 추가하기 전의 LCS 값보다 1을 더해서 저장)
        else:                                           # 두 문자가 다르다면
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])      # 이전까지 비교한 값중 최대값

print(dp[-1][-1])







