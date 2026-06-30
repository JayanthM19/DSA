#https://leetcode.com/problems/distinct-subsequences/

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n,m=len(s),len(t)
#Recursion

        # def solve(i,j):

        #     if j<0:
        #         return 1
        #     if i<0:
        #         return 0
            
        #     if s[i]==t[j]:
        #         return solve(i-1,j-1)+solve(i-1,j)

        #     return solve(i-1,j)

        # return solve(n-1,m-1)

#memoization

        # dp=[[-1]*(m) for _ in range(n)]
        # def solve(i,j):
        #     if j<0:
        #         return 1
        #     if i<0:
        #         return 0
            
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
            
        #     if s[i]==t[j]:
        #         dp[i][j]=solve(i-1,j-1)+solve(i-1,j)
        #     else:
        #         dp[i][j]=solve(i-1,j)
            
        #     return dp[i][j]
        # return solve(n-1,m-1)

#Tabulation

        # dp=[[0]*(m+1) for _ in range(n+1)]

        # for i in range(n+1):
        #     dp[i][0]=1
        
        # for i in range(1,n+1):
        #     for j in range(1,m+1):
        #         if s[i-1]==t[j-1]:
        #             dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
        #         else:
        #             dp[i][j]=dp[i-1][j]

        # return dp[n][m]

#Space optimized1

        # prev=[0]*(m+1)

        # prev[0]=1

        # for i in range(1,n+1):
        #     curr=[0]*(m+1)
        #     curr[0]=1
        #     for j in range(1,m+1):
        #         if s[i-1]==t[j-1]:
        #             curr[j]=prev[j-1]+prev[j]
        #         else:
        #             curr[j]=prev[j]
            
        #     prev=curr
        
        # return curr[m]

#Single array space optimized
        prev=[0]*(m+1)

        prev[0]=1

        for i in range(1,n+1):
            
            for j in range(m,0,-1):
                if s[i-1]==t[j-1]:
                    prev[j]=prev[j-1]+prev[j]
                
        
        return prev[m]

