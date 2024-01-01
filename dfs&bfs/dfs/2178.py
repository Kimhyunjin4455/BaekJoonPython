# 1은 이동 가능 0 은 불가능
# 출발 1,1 => 도착 n,m
from collections import deque

n, m = map(int, input().split())
area = [list(map(int, list(input()))) for _ in range(n)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]
visited = [[0]*m for _ in range(n)]

def bfs(row, col):
    queue = deque()
    queue.append((row, col))

    while queue:
        r,c = queue.popleft()
        visited[r][c] = 1
        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]

            if 0 <=nr <n and 0 <=nc <m and area[nr][nc] == 1 and visited[nr][nc] == 0:
                area[nr][nc] = area[r][c] +1
                queue.append((nr, nc))

    return area[-1][-1]


print(bfs(0,0))
