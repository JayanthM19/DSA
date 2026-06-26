#https://leetcode.com/problems/candy/
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n=len(ratings)
        candy=[1]*(n)

        #Left to right
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                candy[i]=candy[i-1]+1
        
        #rught to left
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                candy[i]=max(candy[i],candy[i+1]+1)


        return sum(candy)

        #example ratings to understand [1,3,4,5,2]



            



            