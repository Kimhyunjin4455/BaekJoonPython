n,m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
result = 1e9
house_arr = []
chicken_arr = []
arr = [] # 치킨거리를 구할 치킨집을 넣을 배열

def cal_distance(arr):
    res = 0
    for h_row, h_col in house_arr: # 집을 기준으로 각 집마다 최소 치킨거리 구하기
        mn_res = 1e9
        for c_row, c_col in arr:
            mn_res = min(mn_res, abs(h_row-c_row) + abs(h_col-c_col))
        res += mn_res
    return res



def dfs(depth, arr):
    global result
    if depth == len(chicken_arr): # 종료되면
        if len(arr) == m:
            result = min(result, cal_distance(arr))
        return

    dfs(depth+1, arr+[chicken_arr[depth]]) # chicken_arr[depth]은 튜플이기에 [] 로 감싸기
    dfs(depth+1, arr)

# 튜플들을 각 배열에 저장
for i in range(n):
    for j in range(n):
        if area[i][j] == 1:
            house_arr.append((i,j))
        if area[i][j] == 2:
            chicken_arr.append((i,j))

dfs(0,[])
print(result)


