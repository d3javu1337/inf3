n = int(input())

d = {}

for i in range(n):
    f = input()
    if(f not in list(d.keys())):
        d[f]=1
    else:
        d[f]+=1
count = 0
for x in list(d.values()):
    if(x>1):
        count+=x
print(count)