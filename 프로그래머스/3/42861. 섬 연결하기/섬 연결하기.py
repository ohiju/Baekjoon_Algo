import heapq

def solution(n, costs):
    ils = [[] for _ in range(n)]
    vst = [0] * n
    
    def dijkstra(N):
        q = [(0,N)]
        dist = 0
        vst[N] = 0
        
        while q:
            d,x = heapq.heappop(q)
            
            if vst[x]:
                continue
            
            vst[x] = 1
            dist += d
            
            for nd,nx in ils[x]:
                if vst[nx]:
                    continue
                heapq.heappush(q, (nd, nx))
        
        return dist
                    
    
    for a,b,c in costs:
        ils[a].append((c,b))
        ils[b].append((c,a))
    
    
    return dijkstra(0)