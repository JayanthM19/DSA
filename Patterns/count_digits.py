#https://takeuforward.org/data-structure/count-digits-in-a-number

import math
class Solution:
    def countDigits(self,n):
        return int(math.log10(n)+1)
    
if __name__=="__main__":
    n=34
    
    sol = Solution()
    print(sol.countDigits(n))
    