#https://leetcode.com/problems/rank-transform-of-an-array/
class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
       
        temp = sorted(set(arr))

        rank = {val: i + 1 for i, val in enumerate(temp)}

        return [rank[num] for num in arr]


        
        
