n = int(input())
nums = list(map(int, input().split()))
rs_incre = [1] * (n)
rs_decre = [1] * (n)

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            rs_incre[i] = max(rs_incre[i], rs_incre[j]+1)

nums.reverse() # 역순으로 증가구하기 == 감소하는 수열 구하기, 또는 for문 역으로 돌리기
for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            rs_decre[i] = max(rs_decre[i], rs_decre[j]+1)
rs_decre.reverse()

def calcul(rs_incre, rs_decre):
    cal = [0] * n
    for i in range(n):
        cal[i] = rs_incre[i] + rs_decre[i]

    return max(cal)

print(calcul(rs_incre, rs_decre)-1)
