n,k=input().split()
n=int(n)
k=int(k)

s=list(input())

if n==1 and k==1:
    s[0]='0'
    k-=1

if n>1 and k>=1 and s[0] != '1':
    k-=1
    s[0]='1'

for i in range(1,n):
    if k==0:
        break
    if s[i]!='0':
        s[i]='0'
        k-=1

print(''.join(s))