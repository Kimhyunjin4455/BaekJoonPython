#LCS
#길이와 문자열 출력
#LCS가 여러 가지인 경우에는 아무거나 출력하고, LCS의 길이가 0인 경우에는 둘째 줄을 출력하지 않는다.

word1 = input()
word2 = input()

l1 = len(word1)
l2 = len(word2)

dp = [['']*(l2+1) for _ in range(l1+1)]


for i in range(1,l1+1):
    for j in range(1,l2+1):
        if word1[i-1] == word2[j-1]:
            dp[i][j] = dp[i-1][j-1] + word1[i-1]    # 문자열 자체를 더해나감 (LCS1문제의 숫자를 더해나가는 것과의 차이)
        else:
            if len(dp[i-1][j]) > len(dp[i][j-1]):   # 문자열의 길이가 더 긴것을 더 함
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]



print(len(dp[-1][-1]))                              # 마지막 인덱스의 문자열 길이가 dp의 결과
if len(dp[-1][-1]) != 0:                            # 문제 요구 조건
    print(dp[-1][-1])