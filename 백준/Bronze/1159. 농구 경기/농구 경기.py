N = int(input())
D = dict()
R = ''

for i in range(N):
    name = input()
    if (name[0]) in D:
        D[name[0]] += 1
    else:
        D[name[0]] = 1

for key, val in D.items():
    if val >= 5:
        R += key

sorted_R = "".join(sorted(R))
if (len(sorted_R) > 0):
    print(sorted_R)
else:
    print('PREDAJA')