import sys
import heapq
input=sys.stdin.readline

n,m = map(int,input().split())
INF = 10**9
arr = [[] for _ in range(n+1)]

def dijkstra(n):
    q = []
    heapq.heappush(q, (0,n))
    dist[n] = (0,-1)

    while q:
        d,x = heapq.heappop(q)

        if d < dist[x][0]:
            continue
            
        for nd,nx in arr[x]:
            new_d = nd + d
            if nx == n or nx == x:
                continue
            if new_d < dist[nx][0]:
                heapq.heappush(q, (new_d, nx))
                if dist[x][1] == -1:
                    dist[nx] = (new_d, nx)
                else:
                    dist[nx] = (new_d, dist[x][1])
            
for _ in range(m):
    a,b,t = map(int,input().split())
    arr[a].append((t,b))
    arr[b].append((t,a))
    
for i in range(1,n+1):
    dist = [(INF,-1)] * (n+1)
    dijkstra(i)
    for j in range(1,n+1):
        if dist[j][1] == - 1:
            print('-', end=' ')
        else:
            print(dist[j][1], end=' ')
    print()