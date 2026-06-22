#https://leetcode.com/problems/coin-change-ii/

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        n=len(coins)

#Recursion
        # def solve(ind , amount):
        #     if amount == 0 :
        #         return 1
        #     if ind==0:
        #         return 1 if amount%coins[0]==0 else 0
            
        #     nottake=solve(ind-1,amount)
        #     take=0
        #     if coins[ind]<=amount:
        #         take=solve(ind,amount-coins[ind])
            
        #     return take+nottake
        # return solve(n-1,amount)

#Memoization

        # dp={}

        # def solve(ind,amount):

        #     if amount==0:
        #         return 1
        #     if ind==0:
        #         return 1 if amount%coins[0]==0 else 0
            
        #     if (ind,amount) in dp:
        #         return dp[(ind,amount)]

        #     nottake=solve(ind-1,amount)
        #     take=0
        #     if amount>=coins[ind]:
        #         take=solve(ind,amount-coins[ind])

        #     dp[(ind,amount)]=take+nottake

        #     return dp[(ind,amount)]
        # return solve(n-1,amount)

#Tabluation


        # dp=[[0]*(amount+1) for _ in range(n+1)]

        # for i in range(n+1):
        #     dp[i][0]=1
        
        # for i in range(amount+1):
        #     if i%coins[0]==0:
        #         dp[0][i]=1
        
        # for i in range(1,n):
        #     for j in range(amount+1):
        #         nottake=dp[i-1][j]

        #         take=0
        #         if j>=coins[i]:
        #             take=dp[i][j-coins[i]]

        #         dp[i][j]=take+nottake

        # return dp[n-1][amount]

#Space optimized

        prev=[0]*(amount+1)
        for j in range(amount + 1):
            if j % coins[0] == 0:
                prev[j] = 1

        for i in range(1,n):
            curr=[0]*(amount+1)
            curr[0]=1
            for j in range(amount+1):

                nottake=prev[j]
                take=0
                if j>=coins[i]:
                    take=curr[j-coins[i]]


                curr[j]=take+nottake

            prev=curr
        
        return prev[amount]