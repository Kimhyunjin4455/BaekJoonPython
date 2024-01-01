# 값 입력
n = int(input())
area = [list(input().split()) for _ in range(n)]
teacher_cnt = 0

# 필요한 정보
dr = [-1,1,0,0]
dc = [0,0,-1,1]
for i in range(n): # 선생의 수 파악 위함
    for j in range(n):
        if area[i][j] == 'T':
            teacher_cnt += 1
result = False


def is_check(row, col):
    for dir in range(4): # 상하좌우 탐색
        nr = row + dr[dir]
        nc = col + dc[dir]
        while 0<=nr<n and 0<=nc<n and area[nr][nc] != 'O': # 공간내에서, 장애물이 없는 동안 진행
            if area[nr][nc] == 'S': # 학생을 만난다면
                return True # 감시 성공
            else: # 학생이 아니라면 '그 방향'으로 계속 탐색
                nr += dr[dir]
                nc += dc[dir]
    return False # 감시 실패 (그 방향에 학생이 없거나, 장애물에 가려짐)



def dfs(depth):
    global result

    if depth == 3: # 3개를 설치했다면
        cnt = 0
        for i in range(n):
            for j in range(n):
                if area[i][j] == 'T': # 선생을 기준으로
                    if not is_check(i,j): # 감시하지 못하면 (is_check()는 감시가 불가능 할 때 False 리턴)
                        cnt += 1
        if cnt == teacher_cnt: # 전부 다 감시하지 못한다면 (장애물 3개 놓기 성공한다면)
            result = True
        return


    for i in range(n): # 장애물 놓기
        for j in range(n):
            if area[i][j] == 'X':
                area[i][j] = 'O'
                dfs(depth+1)
                area[i][j] = 'X' # 원복 처리

dfs(0)

if result:
    print('YES')
else:
    print('NO')