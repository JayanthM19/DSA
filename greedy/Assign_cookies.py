#https://leetcode.com/problems/assign-cookies/description/

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # m,n = len(g), len(s)

        # dp= [[0]*(n+1) for _ in range(m+1)]

        # for i in range(m):
        #     dp[i][0]=1
        
        # dp[0][0]=0

        # for i in range(1,m):
        #     for j in range(1,n):
        #         if g[i]<=s[j]:
        #             dp[i][j]=1+dp[i][j-1]
        #         else:
        #             dp[i][j]=dp[i-1][j]

        # return dp[m][n]
                
        
        g.sort()
        s.sort()

        i,j=0,0

        while i<len(g) and j<len(s):
            if g[i]<=s[j]:
                i+=1
                j+=1
            else:
                j+=1
        
        return i