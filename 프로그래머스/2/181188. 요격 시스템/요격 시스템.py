def solution(targets):
    ans = 0
        
    targets.sort(key = lambda x:x[1])
    camera = -1
    
    for s,e in targets:
        if camera > s:
            continue
            
        if camera < e:
            ans += 1
            camera = e - 0.1
            
    
    return ans