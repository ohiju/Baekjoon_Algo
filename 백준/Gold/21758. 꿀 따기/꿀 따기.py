import sys
from copy import deepcopy
input=sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
Arr = deepcopy(arr)
ans = 0

for i in range(1,N):
    Arr[i] += Arr[i-1]

for i in range(1,N-1):
    ans = max(ans, Arr[-1]*2 - arr[i] - Arr[i] - arr[0])

for i in range(1,N-1):
    ans = max(ans, Arr[-1] + Arr[i] - arr[i] * 2 - arr[-1])

for i in range(1,N-1):
    ans = max(ans, Arr[-1] + arr[i] - arr[0] - arr[-1])

print(ans)