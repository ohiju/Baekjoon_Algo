import sys
import heapq
input=sys.stdin.readline

N = int(input())
INF = 10 ** 9
nodes = [[] for _ in range(N+1)]
max_length = 0

for _ in range(N-1):
    s,e,w = map(int,input().split())
    nodes[s].append((w,e))
    nodes[e].append((w,s))

def dijkstra(n):
    global max_length
    dist = [INF] * (N+1)
    q = [(0,n)]
    dist[n] = 0

    while q:
        d,x = heapq.heappop(q)

        if d > dist[x]:
            continue

        for dst,nx in nodes[x]:
            nd = dst + d
            if nd < dist[nx]:
                dist[nx] = nd
                heapq.heappush(q, (nd,nx))
                if dist[nx] > max_length:
                    max_length = dist[nx]
    
    return dist


# for i in range(1,N+1):
#     dijkstra(i)

# 임의이 노드에서 가장 먼 거리까지 거리를 구한 후, 해당 노드에서 최장 거리를 구하면 그게 곧 트리의 지름
temp = dijkstra(1)[1:]
new_start = temp.index(max(temp))+1
ans = dijkstra(new_start)[1:]

print(max(ans))