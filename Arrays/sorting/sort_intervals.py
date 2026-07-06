#https://leetcode.com/problems/remove-covered-intervals/
class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        count=0
        max_end=0

        intervals.sort(key = lambda x :(x[0],-x[1]))

        for start,end in intervals:

            if end>max_end:
                count+=1
                max_end=end
        
        return count

