class Solution:
    @classmethod
    def check(cls):
        n=int(input())
        while(n>0):
            ans=0
            l=[int(x) for x in input().split()]

            if(l[0]==0 or l[1]==0):
                ans=0

            elif(l[2]==0):
                k1=int(l[1]/2)
                k2=int(l[0]/2)
                if k1>=k2:
                    if k1>=l[0]:
                        ans=k1
                    else:
                        ans=min(k1,l[0])
                else:
                    if k2>=l[1]:
                        ans=k2
                    else:
                        ans=min(l[1],k2)

            else:
                c=min(l[0],l[1],l[2])
                if l[2]==c:
                    l[1]=l[1]-c
                    l[0]=l[0]-c
                    k1 = int(l[1] / 2)
                    k2 = int(l[0] / 2)
                    if k1 >= k2:
                        if l[1] % 2 == 1 and l[0] - k1 >= 2:
                            ans = c+k1 + 1
                        else:
                            ans = min(l[0]+c,c+k1)
                    else:
                        if l[0] % 2 == 1 and l[1] - k2 >= 2:
                            ans = c+k2 + 1
                        else:
                            ans = min(c+k2,c+l[1])
                else:
                    ans=c

            print(ans)

            n=n-1

if __name__ == "__main__":
    Solution.check()