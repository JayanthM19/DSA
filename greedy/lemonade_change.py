#https://leetcode.com/problems/lemonade-change/description/

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        # freq={}
        # for bill in bills:
        #     freq[bill]=freq.get(bill,0)+1
        
        five,ten=0,0

        if bills[0]!=5:
            return False
        
        for x in bills:
            if x==5:
                five+=1
            elif x==10:
                if five>0:
                    five-=1
                else:
                    return False
                ten+=1
            else:
                if five>0 and ten>0:
                    five-=1
                    ten-=1
                elif five>2:
                    five-=3
                else:
                    return False
        
        return True

        