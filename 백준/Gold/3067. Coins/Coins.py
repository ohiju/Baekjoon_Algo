import sys
input=sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    C = list(map(int,input().split()))
    goal = int(input())

    dp = [0 for _ in range(goal+1)]
    dp[0] = 1

    for i in range(N):
        for j in range(C[i], goal+1):
            dp[j] += dp[j-C[i]]

    print(dp[goal])