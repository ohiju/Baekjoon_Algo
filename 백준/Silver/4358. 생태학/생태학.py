dic = dict()

while True:
    try:
        name = input()
    except:
        break

    if name in dic:
        dic[name] += 1
    else:
        dic[name] = 1

value = sum(dic.values())
dic = dict(sorted(dic.items()))

for key in dic:
    a = dic[key]
    per = (a / value * 100)
    print("%s %.4f" %(key, per))