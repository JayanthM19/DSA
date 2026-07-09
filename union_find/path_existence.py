#https://leetcode.com/problems/path-existence-queries-in-a-graph-i/
class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        parent=list(range(n))

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            
            return parent[x]

        def union(a,b):
            pa=find(a)
            pb=find(b)

            if pa!=pb:
                parent[pb]=pa
        
        for i in range(n-1):
            if abs(nums[i]-nums[i+1])<=maxDiff:
                union(i,i+1)

        ans=[]
        for u,v in queries:
            ans.append(find(u)==find(v))

        return ans