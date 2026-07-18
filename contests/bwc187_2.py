class Solution(object):
    def maximumValue(self, n, s, m):
        """
        :type n: int
        :type s: int
        :type m: int
        :rtype: int
        """
        if n==0:
            return 0

        if n==1:
            return s

        if n%2==0:
            return s+(n//2)*m-((n//2)-1)

        else:
            return s+(n//2)*m-((n//2)-1)