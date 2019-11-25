class Solution:
    @classmethod
    def check(cls):
        q=int(input())
        while(q>0):
            n=int(input())
            l=[int(x) for x in input().split()]
            ans="NO"

            flag=True
            while(flag):
                flag=False
                l.sort()
                m=len(l)
                #print(q,l)
                if 2048 in l:
                    ans="YES"
                    flag=False
                    continue
                for i in range(m-1,0,-1):
                    if(l[i]==l[i-1]):
                        flag=True
                        k=l[i]
                        l.pop(i-1)
                        l.pop(i-1)
                        l.append(2*k)

            q=q-1
            print(ans)

if __name__ == "__main__":
    Solution.check()