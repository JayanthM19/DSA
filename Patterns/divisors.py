#https://takeuforward.org/data-structure/print-all-divisors-of-a-given-number
import math
class Solution:
    def divisors(self ,n):
    
        final=[]
        for i in range(1,int(math.sqrt(n))+1):
            if n%i==0:
                final.append(i)
                
                if i!=n//i:
                    final.append(n//i)
        final.sort()
            
        return final
                
            
        
if __name__=="__main__":
    sol=Solution()
    n=56
    print(sol.divisors(n))