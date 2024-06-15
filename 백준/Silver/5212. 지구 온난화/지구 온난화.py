import sys
input=sys.stdin.readline

R,C = map(int,input().split())
arr = [list(map(str,input().strip())) for _ in range(R)]
vst = [[0]*C for _ in range(R)]

mr = 0
mc = 0
lr = 11
lc = 11

def check(a,b):
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]

    cnt = 0
    for k in range(4):
        nx = a + dx[k]
        ny = b + dy[k]
        if 0<=nx<R and 0<=ny<C:
            if arr[nx][ny] == '.':
                cnt += 1
        else:
            cnt += 1
    
    if cnt >= 3:
        vst[a][b] = 1    
    
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'X':
            check(i,j)

for i in range(R):
    for j in range(C):
        if vst[i][j]:
            arr[i][j] = '.'
        if arr[i][j] == 'X':
            if i < lr:
                lr = i
            if i > mr:
                mr = i
            if j < lc:
                lc = j
            if j > mc:
                mc = j
        
for i in range(lr,mr+1):
    for j in range(lc,mc+1):
        print(arr[i][j], end='')
    print()