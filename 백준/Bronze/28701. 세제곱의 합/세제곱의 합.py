N = int(input())
print(N*(N+1) // 2)
S = 0
for i in range(N+1):
    S += i**3
    
print(S)
print(S)