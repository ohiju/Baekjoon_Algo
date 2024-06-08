import sys
input=sys.stdin.readline

M,N = map(int,input().split())
arr = [list(map(int,input().strip())) for _ in range(M)]
arr2 = [[0]*(N+2) for _ in range(M+2)]
dp = [[0]*(N+2) for _ in range(M+2)]

for i in range(1,M+1):
    arr2[i][1] = arr[i-1][0]

ans = 0
for j in range(1,N+1):
    for i in range(1,M+1):
        dp[i][j] = max(arr2[i-1][j-1], arr2[i][j-1], arr2[i+1][j-1])
        arr2[i][j] = dp[i][j] + arr[i-1][j-1]

        ans = max(ans, dp[i][j])

print(ans)