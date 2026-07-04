#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)

#Recursion
        # def solve(ind,buy):
        #     if ind>=n:
        #         return 0
            
        #     if buy:
        #         profit=max(-prices[ind]+solve(ind+1,0),solve(ind+1,1))
        #     else:
        #         profit=max(prices[ind]+solve(ind+2,1),solve(ind+1,0))

        #     return profit

        # return solve(0,1)

#Memoization

        # dp=[[-1]*2 for _ in range(n)]
        # def solve(ind,buy):
        #     if ind>=n:
        #         return 0
        #     if dp[ind][buy]!=-1:
        #         return dp[ind][buy]
            
        #     if buy:
        #         profit=max(-prices[ind]+solve(ind+1,0),solve(ind+1,1))
        #     else:
        #         profit=max(prices[ind]+solve(ind+2,1),solve(ind+1,0))

        #     dp[ind][buy]=profit

        #     return dp[ind][buy]

        # return solve(0,1)

#Tabulation

        # dp=[[0]*2 for _ in range(n+2)]

        # for i in range(n-1,-1,-1):
            
        #         dp[i][0]=max(prices[i]+dp[i+2][1],dp[i+1][0])
        #         dp[i][1]=max(-prices[i]+dp[i+1][0],dp[i+1][1])

        # return dp[0][1]

#Space Optimization

        ahead1=[0]*2
        ahead2=[0]*2

        for i in range(n-1,-1,-1):
            curr=[0]*2

            curr[0] = max(
                prices[i] + ahead2[1],
                ahead1[0]
            )

            curr[1] = max(
                -prices[i] + ahead1[0],
                ahead1[1]
            )

            ahead2=ahead1
            ahead1=curr
        
        return ahead1[1]
            
