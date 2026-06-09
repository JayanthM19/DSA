#https://takeuforward.org/data-structure/check-if-a-number-is-prime-or-not

class Solution:
    def Prime(self,n):
        final=0
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                final+=1
                if i!=n//i:
                    final+=1
        return final==2
if __name__=="__main__":
    
    sol=Solution()
    n=79
    print(sol.Prime(n))