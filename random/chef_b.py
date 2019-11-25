class Solution:
    @classmethod
    def check(cls):
        t=int(input())
        while(t>0):
            t-=1
            n=int(input())
            l=[int(x) for x in input().split()]
            x=int(input())
            i=0
            j=n-1
            while(i<n and j>=0 and i<j):
                if l[i]>0:
                    l[i]=l[i]-x
                else:
                    i+=1
                    if i==j:
                        ans=[i,n-j]
                        print(i,n-j)
                        return
                    else:
                        l[i]=l[i]-x
                if l[j]>0:
                    l[j]=l[j]-1
                else:
                    j-=1
                    if j==i:
                        ans=[i+1,n-1-j]
                        print(i+1, n-1 - j)
                        return
                    else:
                        l[j]=l[j]-1
            ans=[i,n-1-j]
            print(i,n-1-j)
            return

if __name__ == "__main__":
    Solution.check()

