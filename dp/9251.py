# LCS
# 두 문자열
words1 = input()
words2 = input()

l1 = len(words1)
l2 = len(words2)
dp = [0] * max(l1,l2)

for i in range(l1):
    cnt = 0
    for j in range(l2):
        if cnt < dp[j]:
            cnt = dp[j] # 글자가 다른 경우 => 누적값이 해당 위치의 값보다 작다면 해당 위치의 값으로 교체
        elif words1[i] == words2[j]: # 순회하면서 만나는 문자열이 같다면
            dp[j] = cnt + 1 # 이전까지의 최댓값 +1

print(max(dp))






