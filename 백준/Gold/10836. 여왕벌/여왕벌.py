import sys
input=sys.stdin.readline

M,N = map(int,input().split())
arr = [1] * (2*M - 1)

for _ in range(N):
    a,b,c = map(int,input().split())

    for i in range(a,a+b):
        arr[i] += 1
    
    for i in range(a+b,a+b+c):
        arr[i] += 2

for i in range(M):
    for j in range(M):
        if j == 0:
            print(arr[M - i - 1], end = ' ')
        else:
            print(arr[M + j - 1], end = ' ')
    print()