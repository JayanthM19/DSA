#https://leetcode.com/problems/wildcard-matching/

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        m,n=len(p),len(s)

#Recursion

        # def solve(i,j):
        #     if i<0 and j<0:
        #         return True
            
        #     if i<0 and j>=0:
        #         return False
            
        #     if j<0 and i>=0:
        #         for k in range(i+1):
        #             if p[k]!="*":
        #                 return False
        #         return True

        #     if p[i]==s[j] or p[i]=="?":
        #         return solve(i-1,j-1)

        #     if p[i]=="*":
        #         return solve(i-1,j) or solve(i,j-1)

        #     return False



        # return solve(m-1,n-1)
        
        
#Memoization

        # dp=[[-1]*(n) for _ in range(m)]

        # def solve(i,j):
        #     if i<0 and j<0:
        #         return True
            
        #     if i<0 and j>=0:
        #         return False
            
        #     if j<0 and i>=0:
        #         for k in range(i+1):
        #             if p[k]!="*":
        #                 return False
                
        #         return True
            
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
            
        #     if p[i]==s[j] or p[i]=="?":
        #         dp[i][j]=solve(i-1,j-1)
        #     elif p[i]=="*":
        #         dp[i][j]=solve(i,j-1) or solve(i-1,j)
        #     else:
        #         dp[i][j]=False
            
        #     return dp[i][j]

        # return solve(m-1,n-1)

#Tabulation

        # dp=[[False]*(n+1) for _ in range(m+1)]

        # dp[0][0]=True

        # for i in range(1,m+1):

        #     for k in range(1,i+1):
        #         flag=True
        #         if p[k-1]!="*":
        #             flag=False
        #             break
        
        #     dp[i][0]=flag

        # for i in range(1,m+1):
        #     for j in range(1,n+1):

        #         if p[i-1]==s[j-1] or p[i-1]=="?":
        #             dp[i][j]=dp[i-1][j-1]
                
        #         elif p[i-1]=="*":
        #             dp[i][j]=dp[i-1][j] or dp[i][j-1]
                
        #         else:
        #             dp[i][j]=False
        
        # return dp[m][n]

#Space optimized

        # prev=[False]*(n+1)

        # prev[0] = True


        # for i in range(1,m+1):
        #     curr=[False]*(n+1)

        #     curr[0]=True
        #     flag=True
        #     for k in range(1, i + 1):
        #         if p[k - 1] != "*":
        #             flag = False
        #             break

        #     curr[0] = flag
        #     for j in range(1,n+1):

        #         if p[i-1]==s[j-1] or p[i-1]=="?":
        #             curr[j]=prev[j-1]
                
        #         elif p[i-1]=="*":
        #             curr[j]=prev[j] or curr[j-1]
                
        #         else:
        #             curr[j]=False
            
        #     prev=curr
        
        # return prev[n]

            
      