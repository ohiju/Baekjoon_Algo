import sys
input=sys.stdin.readline

N = int(input())
arr = [[] for _ in range(N+1)]

for i in range(1,N+1):
    n = int(input())
    arr[i].append(n)

def dfs(num):
    global ans
    if vst[num] == False:
        vst[num] = 1

        for x in arr[num]:
            A.add(num)
            B.add(x)

            if A == B:
                ans.extend(list(A))
                return 
            
            dfs(x)
    vst[num] = False

ans = []
for i in range(1,N+1):
    vst = [0] * (N+1)
    A = set()
    B = set()

    dfs(i)

ans = list(set(ans))
ans.sort()

print(len(ans))
for a in ans:
    print(a)