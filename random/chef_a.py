class Solution:
    @classmethod
    def check(cls):
        t=int(input())
        while(t>0):
            t-=1
            n=int(input())
            l=[int(x) for x in input().split()]
            ans=[0]*n
            k=-1
            for i in range(n-2,-1,-1):
                if l[i]==l[i+1]:
                    ans[i]=ans[i+1]
                else:
                    if k==-1:
                        ans[i]=n-1-i
                        k=i
                    else:
                        ans[i]=ans[i+1]+k-i
                        k=i
            res=""
            for i in range(n):
                res=res+str(ans[i])+" "
            print(res)




if __name__ == "__main__":
    Solution.check()

