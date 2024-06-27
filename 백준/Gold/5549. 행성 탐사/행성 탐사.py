import sys
input=sys.stdin.readline

M,N = map(int,input().split())
K = int(input())
arr = [list(map(str,input().strip())) for _ in range(M)]
Jsum, Osum, Isum = [[0]*(N+1) for _ in range(M+1)],[[0]*(N+1) for _ in range(M+1)],[[0]*(N+1) for _ in range(M+1)]

for i in range(M):
    for j in range(N):
        if arr[i][j] == 'J':
            Jsum[i+1][j+1] += 1
        elif arr[i][j] == 'O':
            Osum[i+1][j+1] += 1
        elif arr[i][j] == 'I':
            Isum[i+1][j+1] += 1
        Jsum[i+1][j+1] += Jsum[i][j+1] + Jsum[i+1][j] - Jsum[i][j]
        Osum[i+1][j+1] += Osum[i][j+1] + Osum[i+1][j] - Osum[i][j]
        Isum[i+1][j+1] += Isum[i][j+1] + Isum[i+1][j] - Isum[i][j]

for _ in range(K):
    a,b,c,d = map(int,input().split())

    print(Jsum[c][d]-Jsum[a-1][d]-Jsum[c][b-1]+Jsum[a-1][b-1], Osum[c][d]-Osum[a-1][d]-Osum[c][b-1]+Osum[a-1][b-1], Isum[c][d]-Isum[a-1][d]-Isum[c][b-1]+Isum[a-1][b-1])