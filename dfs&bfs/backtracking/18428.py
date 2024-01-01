# 값 입력
n = int(input())
area = [list(input().split()) for _ in range(n)]
teacher_cnt = 0

# 필요힌 정보
dr = [-1,1,0,0]
dc = [0,0,-1,1]
for i in range(n):
    for j in range(n):
        if area[i][j] == 'T':
            teacher_cnt += 1
result = False


def is_check(row, col):
    for dir in range(4):
        nr = row + dr[dir]
        nc = col + dc[dir]
        while 0<=nr<n and 0<=nc<n and area[nr][nc] != 'O':
            if area[nr][nc] == 'S':
                return True
            else: # 학생이 아니라면 그 방향으로 계속 탐색
                nr += dr[dir]
                nc += dc[dir]
    return False



def dfs(depth):
    global result

    if depth == 3:
        cnt = 0
        for i in range(n):
            for j in range(n):
                if area[i][j] == 'T':
                    if not is_check(i,j): # 감시하지 못하면
                        cnt += 1
        if cnt == teacher_cnt:
            result = True
        return


    for i in range(n):
        for j in range(n):
            if area[i][j] == 'X':
                area[i][j] = 'O'
                dfs(depth+1)
                area[i][j] = 'X'

dfs(0)

if result:
    print('YES')
else:
    print('NO')