import sys
from collections import deque
input=sys.stdin.readline

N,M = map(int, input().split())
x1,y1,x2,y2 = map(int, input().split())
x1 -= 1
y1 -= 1
arr = [[] for _ in range(N)]

for i in range(N):
    sa = input()
    for j in range(M):
        if sa[j] == '1' or sa[j] == '0':
            arr[i].append(int(sa[j]))
        elif sa[j] == '#':
            arr[i].append(2)
        elif sa[j] == '*':
            arr[i].append(3)

def bfs():
    q = deque()
    q.append((x1,y1))
    vst = [[0]*M for _ in range(N)]
    vst[x1][y1] = 1

    dx = [-1,1,0,0]
    dy = [0,0,1,-1]

    while q:
        x,y = q.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0<=nx<N and 0<=ny<M:
                if arr[nx][ny] == 2:
                    return True
                if vst[nx][ny] == 0 and arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                    vst[nx][ny] = 1
                if vst[nx][ny] == 0 and arr[nx][ny] == 0:
                    vst[nx][ny] = 1
                    q.append((nx,ny))

    return False

cnt = 1
while True:
    if bfs():
        print(cnt)
        break
    cnt += 1
