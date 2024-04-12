a = list(set(input().split('; ')))

a = [str(b) for b in sorted([int(x) for x in a])]

d ={}

def getDen(c: str):
    c = int(c)
    s = set()
    for x in range(1,c+1):
        if(c%x==0):
            s.add(x)
    return s


for x in a:
    for y in a:
        if(getDen(x) & getDen(y) == {1}):
            if(x not in d):
                d[x] = []
            d[x].append(y)

for x in list(d.keys()):
    if(len(d[x])!=0):
        print(f'{x} - {", ".join(d[x])}')
