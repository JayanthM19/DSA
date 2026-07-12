#https://leetcode.com/problems/minimum-cost-to-cut-a-stickko/
class Solution(object):
    def minCost(self, n, cuts):
        """
        :type n: int
        :type cuts: List[int]
        :rtype: int
        """
        
        
        m=len(cuts)
        cuts.insert(0,0)
        cuts.append(n)

        cuts.sort()

#Recursion    

        # def solve(i,j):
        #     if i>j:
        #         return 0
            
        #     mini=float('inf')

        #     for k in range(i,j+1):
        #         cost=cuts[j+1]-cuts[i-1]+solve(i,k-1)+solve(k+1,j)

        #         mini=min(mini,cost)

        #     return mini

        # return solve(1,m)

#Memoization

        # dp=[[-1]*n for _ in range(n)]
        # def solve(i,j):
        #     if i>j:
        #         return 0
            
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
        #     mini=float('inf')

        #     for k in range(i,j+1):
        #         cost=cuts[j+1]-cuts[i-1]+solve(i,k-1)+solve(k+1,j)

        #         mini=min(mini,cost)

        #     dp[i][j]=mini
        #     return dp[i][j]

        # return solve(1,m)
        
        
#Tabulation

        dp=[[0]*(m+2) for _ in range(m+2)]

        
        for i in range(m,0,-1):
            for j in range(1,m+1):
                if i>j:
                    continue
                
                mini=float('inf')

                for k in range(i,j+1):
                    cost=cuts[j+1]-cuts[i-1]+dp[i][k-1]+dp[k+1][j]#solve(i,k-1)+solve(k+1,j)

                    mini=min(mini,cost)

                dp[i][j]=mini
        
        return dp[1][m]
            
