from collections import deque

def solution(maps):
    ans = 0
    m = len(maps)
    n = len(maps[0])
    
    def dfs(a,b,goal):
        vst = [[0]*n for _ in range(m)]
        vst[a][b] = 1 
        q = deque()
        q.append((a,b))
        
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        
        while q:
            x,y = q.popleft()
            
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0<=nx<m and 0<=ny<n:
                    if maps[nx][ny] == goal:
                        return vst[x][y]
                    elif (maps[nx][ny] != 'X' and vst[nx][ny] == 0):
                        vst[nx][ny] = vst[x][y] + 1
                        q.append((nx,ny))
                    
        return -1
                        
        
    for i in range(m):
        for j in range(n):
            if maps[i][j] == 'S':
                temp = dfs(i,j,'L')
                if temp == -1:
                    return -1
                else:
                    ans += temp
                
    for i in range(m):
        for j in range(n):
            if maps[i][j] == 'L':
                temp = dfs(i,j,'E')
                if temp == -1:
                    return -1
                else:
                    ans += temp
    
    return ans