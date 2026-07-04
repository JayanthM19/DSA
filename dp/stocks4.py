#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """

#Recursion       
        n=len(prices)

        # def solve(ind,buy,trans):
        #     if trans==k:
        #         return 0
            
        #     if ind==n:
        #         return 0
            
        #     if buy:
        #         profit=max(-prices[ind]+solve(ind+1,0,trans),solve(ind+1,1,trans))
        #     else:
        #         profit=max(prices[ind]+solve(ind+1,1,trans+1),solve(ind+1,0,trans))

        #     return profit

        # return solve(0,1,0)

#Memoization

        # dp=[[[-1]*k for _ in range(2)]for _ in range(n)]
        # def solve(ind,buy,trans):
        #     if trans==k:
        #         return 0
            
        #     if ind==n:
        #         return 0

        #     if dp[ind][buy][trans]!=-1:
        #         return dp[ind][buy][trans]
            
        #     if buy:
        #         profit=max(-prices[ind]+solve(ind+1,0,trans),solve(ind+1,1,trans))
        #     else:
        #         profit=max(prices[ind]+solve(ind+1,1,trans+1),solve(ind+1,0,trans))

        #     dp[ind][buy][trans]=profit
        #     return dp[ind][buy][trans]

        # return solve(0,1,0)


#Tabulation 

        # dp=[[[0]*(k+1) for _ in range(2)]for _ in range(n+1)]

        # for i in range(n-1,-1,-1):
        #     for j in range(k):
        #         dp[i][1][j]=max(-prices[i]+dp[i+1][0][j],dp[i+1][1][j])

        #         dp[i][0][j]=max(prices[i]+dp[i+1][1][j+1],dp[i+1][0][j])

        # return dp[0][1][0]


#Space Optimization

        ahead=[[0]*(k+1)for _ in range(2)]

        for i in range(n-1,-1,-1):
            curr=[[0]*(k+1)for _ in range(2)]

            for j in range(k):
                curr[1][j]=max(-prices[i]+ahead[0][j],ahead[1][j])

                curr[0][j]=max(prices[i]+ahead[1][j+1],ahead[0][j])
            
            ahead=curr

        return ahead[1][0]
