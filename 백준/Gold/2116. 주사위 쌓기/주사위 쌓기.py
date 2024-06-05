import sys
input=sys.stdin.readline

N = int(input())
arr = []

def dice(n):
    if n == 0:
        return 5
    elif n == 1:
        return 3
    elif n == 2:
        return 4
    elif n == 3:
        return 1
    elif n == 4:
        return 2
    elif n == 5:
        return 0

for i in range(N):
    a = list(map(int,input().split()))
    arr.append(a)

ans = 0
for i in range(6):
    s = arr[0][i]
    e = arr[0][dice(i)]
    m = 0
    tmp_ans = 0

    for j in range(6):
        if j != i and j != dice(i):
            if m < arr[0][j]:
                m = arr[0][j]
    tmp_ans += m

    for k in range(1,N):
        save_1 = -1
        save_2 = -1
        for l in range(6):
            if arr[k][l] == e:
                s = e
                e = arr[k][dice(l)]
                save_1 = l
                save_2 = dice(l)
                break
        nm = 0
        for x in range(6):
            if x != save_1 and x != save_2:
                if nm < arr[k][x]:
                    nm = arr[k][x]
        tmp_ans += nm
    
    if tmp_ans > ans:
        ans = tmp_ans

print(ans)