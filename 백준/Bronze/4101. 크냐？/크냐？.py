while True:
    m,n = map(int,input().split())
    
    if m == 0 and n == 0:
        exit()
        
    if m > n:
        print('Yes')
    else:
        print('No')