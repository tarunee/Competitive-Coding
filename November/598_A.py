q=int(input())

while q>0:
    q=q-1

    # indices-variable 0-a 1-b 2-n 3-S
    l = [int(x) for x in input().split()]

    x=l[0]*l[2]

    if x==l[3]:
        print("YES")
    elif x<l[3]:
        if x+l[1]>=l[3]:
            print("YES")
        else:
            print("NO")
    else:
        s=l[3]/l[2]
        r = l[3] % l[2]
        if r<=l[1] and s<=l[0]:
            print("YES")
        else:
            print("NO")