class Solution(object):
    def maxDistance(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        
        return abs(moves.count('R')-moves.count('L'))+abs(moves.count('U')-moves.count('D'))+moves.count('_')©leetcode