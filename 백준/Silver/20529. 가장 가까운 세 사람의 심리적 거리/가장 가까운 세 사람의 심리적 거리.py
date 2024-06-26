import sys
input=sys.stdin.readline

T = int(input())

def check(a,b):
    cnt = 0
    for x in range(4):
        if a[x] != b[x]:
            cnt += 1
    return cnt

for tc in range(T):
    N = int(input())
    arr = list(map(str,input().split()))

    if N > 32:
        print(0)
    else:
        ans = 100
        for i in range(N):
            for j in range(i+1,N):
                for k in range(j+1,N):
                    tmp = 0
                    tmp += check(arr[i], arr[j])
                    tmp += check(arr[k], arr[j])
                    tmp += check(arr[i], arr[k])
                    ans = min(ans, tmp)
        print(ans)