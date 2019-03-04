import random

def typo(str):
    res = []
    for i in str.split('　'):
        if len(i) < 4:
            res.append(i)
        else:
            l = list(i[1:-1])
            random.shuffle(l)
            res.append(i[0] + ''.join(l) + i[-1])
    return '　'.join(res)

str = input()
res = typo(str)
print(res)