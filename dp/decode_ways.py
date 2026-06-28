#https://leetcode.com/problems/decode-ways/

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        n=len(s)
        # dp={}

        # def solve(i):
        #     if i==n:
        #         return 1
            
        #     if s[i]=='0':
        #         return 0
            
        #     if i in dp:
        #         return dp[i]
            
        #     ans = solve(i+1)

        #     if i+1 < n and 10<=int(s[i:i+2])<=26:
        #         ans+=solve(i+2)

        #     dp[i]=ans
        #     return dp[i]
            


        # return solve(0)


        
        
