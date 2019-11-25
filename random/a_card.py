n = int(input())
s = input()
z = 0
e = 0
for i in range(n):
    if s[i] == 'z':
        z = z + 1
    elif s[i] == 'n':
        e = e + 1

ans = ""
for i in range(e):
    ans = ans + '1' + " "

for i in range(z):
    ans = ans + '0' + " "

print(ans)