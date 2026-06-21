class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
#RecursionMethod
        n=len(coins)
        # def solve(ind , amount):
            
            # if amount==0:
            #     return 0
            # if ind==0:
            #     if amount%coins[ind]==0:
            #         return amount//coins[ind]
            #     return float('inf')
            
        #     nottake=solve(ind-1,amount)
        #     take=float('inf')
        #     if amount>=coins[ind]:
        #         take = 1+solve(ind,amount-coins[ind])
            
        #     return min(take,nottake)
        # ans= solve(n-1,amount)

        # return -1 if ans==float('inf') else ans 

#Memoization


        # dp={}

        # def solve(ind , amount):
            
        #     if amount==0:
        #         return 0
        #     if ind==0:
        #         if amount%coins[ind]==0:

        #             return amount//coins[ind]
        #         return float('inf')

        #     if (ind,amount) in dp:
        #         return dp[(ind,amount)]
            
        #     nottake = solve(ind-1,amount)

        #     take=float('inf')

        #     if amount>=coins[ind]:
        #         take=1+solve(ind,amount-coins[ind])
            
        #     dp[(ind,amount)]=min(take,nottake)

        #     return dp[(ind,amount)]
        
        # ans=solve(n-1,amount)

        # return -1 if ans==float('inf') else ans
        


#Tabulation


        # dp=[[float('inf')]*(amount+1) for _ in range(n)]

        
        # for i in range(n):
        #     dp[i][0] = 0
        
        # for i in range(amount+1):
        #     if i%coins[0]==0:
        #         dp[0][i]=i//coins[0]
            
        

        # for i in range(1,n):
        #     for j in range(1,amount+1):
        #         nottake=dp[i-1][j]

        #         take=float('inf')
        #         if j>=coins[i]:
        #             take=1+dp[i][j-coins[i]]
                
        #         dp[i][j]=min(take,nottake)
        
        # return -1 if dp[n-1][amount]==float('inf') else dp[n-1][amount]



#Space Optimized version

        prev = [float('inf')]*(amount+1)

        prev[0]=0

        for i in range(amount+1):
            if i%coins[0]==0:
                prev[i]=i//coins[0]

        for i in range(1,n):
            curr = [float('inf')]*(amount+1)
            curr[0]=0

            for j in range(1,amount+1):
                nottake=prev[j]

                take=float('inf')
                if j>=coins[i]:
                    take=1+curr[j-coins[i]]
                
                curr[j]=min(take,nottake)
            
            prev=curr
        
        return -1 if prev[amount]==float('inf') else prev[amount]


