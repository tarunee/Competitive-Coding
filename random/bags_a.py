l=[int(x) for x in input().split()]

l.sort()

c=l[0]+l[1]+l[2]
if l[0]+l[3]==l[1]+l[2]:
     print("YES")
elif c==l[3]:
    print("YES")
else:
    print("NO")