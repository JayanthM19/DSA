#Solve stocks2 first
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)

        # def solve(ind,buy,transactions):

        #     if transactions==2:
        #         return 0
            
        #     if ind==n:
        #         return 0
            
        #     if buy:
        #         profit = max(-prices[ind]+solve(ind+1,0,transactions),0+solve(ind+1,1,transactions))
        #     else:
        #         profit=max(prices[ind]+solve(ind+1,1,transactions+1),0+solve(ind+1,0,transactions))
            
        #     return profit

        # return solve(0,1,0)

#Memoization

        # dp=[[[-1]*3 for _ in range(2)]for _ in range(n)]
        # def solve(ind,buy,transactions):

        #     if transactions==2:
        #         return 0
            
        #     if ind==n:
        #         return 0

        #     if dp[ind][buy][transactions]!=-1:
        #         return dp[ind][buy][transactions]
            
        #     if buy:
        #         profit = max(-prices[ind]+solve(ind+1,0,transactions),0+solve(ind+1,1,transactions))
        #     else:
        #         profit=max(prices[ind]+solve(ind+1,1,transactions+1),0+solve(ind+1,0,transactions))
            
        #     dp[ind][buy][transactions]=profit

        #     return dp[ind][buy][transactions]

        # return solve(0,1,0)

#Tabulation

        # dp=[[[0]*3 for _ in range(2)]for _ in range(n+1)]

        
        # for i in range(n-1,-1,-1):
        #     for j in range(2):
        #         dp[i][1][j]=max(-prices[i]+dp[i+1][0][j],dp[i+1][1][j])
           
        #         dp[i][0][j]=max(prices[i]+dp[i+1][1][j+1],dp[i+1][0][j])

        # return dp[0][1][0]
            

#Space Optimization
        dp=[[[0]*3 for _ in range(2)]for _ in range(n+1)]

        ahead=[[0]*3 for _ in range(2)]
        for i in range(n-1,-1,-1):
            curr=[[0]*3 for _ in range(2)]
            for j in range(2):
                curr[1][j]=max(-prices[i]+ahead[0][j],ahead[1][j])
           
                curr[0][j]=max(prices[i]+ahead[1][j+1],ahead[0][j])

            ahead=curr

        return ahead[1][0]

        
