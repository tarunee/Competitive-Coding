import math

n=int(input())
m=[]
for i in range(n):
    l=[int(x) for x in input().split()]
    m.append(l)

l=[]
for i in range(0,n-2):
    x=m[i][i+1]/m[i+1][i+2]
    x=x*m[i][i+2]
    x=math.sqrt(x)
    l.append(int(x))

l.append(int(m[0][n-2]/l[0]))
l.append(int(m[0][n-1]/l[0]))

ans=""
for i in range(n):
    ans=ans+str(l[i])+" "

print(ans)