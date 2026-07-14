#https://leetcode.com/problems/palindrome-partitioning-ii/description/
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)

#Recursion
        # def solve(i):
        #     if i==n:
        #         return 0

        #     def isPalindrome(temp):
        #         return temp==temp[::-1]

            
        #     temp=""
        #     min_cost=float('inf')

        #     for j in range(i,n):
        #         temp+=s[j]
        #         if isPalindrome(temp):
        #             cost=1+solve(j+1)
        #             min_cost=min(cost,min_cost)

        #     return min_cost



        # return solve(0)-1

#Memoization

        # dp=[-1]*n
        # def solve(i):
        #     if i==n:
        #         return 0

        #     if dp[i]!=-1:
        #         return dp[i]
            
        #     def isPalindrome(temp):
        #         return temp==temp[::-1]

            
        #     temp=""
        #     min_cost=float('inf')

        #     for j in range(i,n):
        #         temp+=s[j]
        #         if isPalindrome(temp):
        #             cost=1+solve(j+1)
        #             min_cost=min(cost,min_cost)

        #     dp[i]=min_cost

        #     return dp[i]



        # return solve(0)-1

#Tabulation

        dp=[0]*(n+1)

        for i in range(n-1,-1,-1):
            temp=""
            min_cost=float('inf')

            


            for j in range(i,n):    #Same as recursion , no bottom up
                temp+=s[j]
                if temp==temp[::-1]:
                    cost=1+dp[j+1]
                    min_cost=min(cost,min_cost)
            
            dp[i]=min_cost
        
        return dp[0]-1



