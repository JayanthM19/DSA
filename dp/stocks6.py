#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n=len(prices)
#Recusrion
        # def solve(ind,buy):
        #     if ind==n:
        #         return 0
            
        #     if buy:
        #         profit=max(-prices[ind]-fee+solve(ind+1,0),solve(ind+1,1))
        #     else:
        #         profit=max(prices[ind]+solve(ind+1,1),solve(ind+1,0))
            
        #     return profit
        # return solve(0,1)

#Memoization
        # dp=[[-1]*2 for _ in range(n)]
        # def solve(ind,buy):
        #     if ind==n:
        #         return 0
        #     if dp[ind][buy]!=-1:
        #         return dp[ind][buy]
            
        #     if buy:
        #         profit=max(-prices[ind]-fee+solve(ind+1,0),solve(ind+1,1))
        #     else:
        #         profit=max(prices[ind]+solve(ind+1,1),solve(ind+1,0))
            
        #     dp[ind][buy]=profit
        #     return dp[ind][buy]
        # return solve(0,1)

#Tabulation

        # dp=[[0]*2 for _ in range(n+1)]

        # for i in range(n-1,-1,-1):
        #     dp[i][1]=max(-prices[i]-fee+dp[i+1][0],dp[i+1][1])
        #     dp[i][0]=max(prices[i]+dp[i+1][1],dp[i+1][0])

        # return dp[0][1]

#Space optimization

        ahead=[0]*2

        for i in range(n-1,-1,-1):
            curr=[0]*2

            curr[1]=max(-prices[i]-fee+ahead[0],ahead[1])
            curr[0]=max(prices[i]+ahead[1],ahead[0])

            ahead=curr
        
        return ahead[1]
