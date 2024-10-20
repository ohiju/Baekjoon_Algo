N = int(input())

for _ in range(N):
    a = input()
    if 6 <= len(a) and len(a) <= 9:
        print('yes')
    else:
        print('no')