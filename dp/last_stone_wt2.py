#https://leetcode.com/problems/last-stone-weight-ii/

class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n=len(stones)
        total=sum(stones)

        #s1+s2=total
        #s1-s2=0
        #s1=total//2
        #2s1-total=min

#Recursion       

        # def solve(ind,curr):

        #     if ind<0:
        #         return abs(total-2*curr)


        #     nottake=solve(ind-1,curr)
        #     take=solve(ind-1,curr+stones[ind])

        #     return min(take,nottake)


        # return solve(n-1,0)

#Memoization

        # dp={}

        # def solve(ind,curr):
        #     if ind<0:
        #         return abs(total-2*curr)

        #     if (ind,curr) in dp:
        #         return dp[(ind,curr)]

        #     nottake=solve(ind-1,curr)
        #     take=solve(ind-1,curr+stones[ind])

        #     ans=min(take,nottake)

        #     dp[(ind,curr)]=ans

        #     return dp[(ind,curr)]    
        # return solve(n-1,0)

#Tabulation

        dp=[[0]*(total+1) for _ in range(n+1)]

        dp[0][0]=1

        for i in range(1,n+1):
            for j in range(total+1):
                nottake=dp[i-1][j]
                
                take=0
                if stones[i-1]<=j:

                    take=dp[i-1][j-stones[i-1]]
                
                dp[i][j]=take or nottake
        
        target = total//2

        for s1 in range(target,-1,-1):

            if dp[n][s1]:
                return total - 2*s1

        




        





        