#https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        n=len(days)
#Recursion
        # def solve(i):
        #     if i>=n:
        #         return 0
            
        #     j=i
        #     while j<n and days[j]<days[i]+1:
        #         j+=1

        #     one = costs[0]+solve(j)

        #     j=i
        #     while j<n and days[j]<days[i]+7:
        #         j+=1

        #     seven = costs[1]+solve(j)

        #     j=i
        #     while j<n and days[j]<days[i]+30:
        #         j+=1

        #     thirty = costs[2]+solve(j)


        #     return min(one,seven,thirty)
        # return solve(0)


#Memoization

        # dp=[-1]*(n+1)
        # def solve(i):
        #     if i>=n:
        #         return 0
            
        #     if dp[i]!=-1:
        #         return dp[i]

        #     j=i
        #     while j<n and days[j]<days[i]+1:
        #         j+=1
        #     one = costs[0]+solve(j)

        #     j=i
        #     while j<n and days[j]<days[i]+7:
        #         j+=1
        #     seven= costs[1]+solve(j)

        #     j=i
        #     while j<n and days[j]<days[i]+30:
        #         j+=1
        #     thirty = costs[2]+solve(j)

        #     dp[i]=min(one,seven,thirty)

        #     return dp[i]
        # return solve(0)

#Tabulation

        dp=[0]*(n+1)

        

        for i in range(n-1,-1,-1):
            j=i

            while j<n and days[j]<days[i]+1:
                j+=1

            one=costs[0]+dp[j]

            j=i
            while j<n and days[j]<days[i]+7:
                j+=1
            seven = costs[1]+dp[j]

            j=i
            while j<n and days[j]<days[i]+30:
                j+=1
            thirty=dp[j]+costs[2]

            dp[i]=min(one,seven,thirty)
            
        
        return dp[0]

